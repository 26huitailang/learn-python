#!/usr/bin/python
# coding: utf-8

import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request  # 跟进URL的时候用
from dingdian_scrapy.items import DingdianScrapyItem, DcontentItem
from dingdian_scrapy.mysqlpipelines.sql import Sql


class Myspider(scrapy.Spider):

    name = 'dingdian'  # entrypoint.py中的对应的第三个参数
    allowed_domains = ['23us.com']
    bash_url = 'http://www.23us.com/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            # 使用Request包，跟进URL（返回的response作为参数传递给self.parse, 这个叫回调函数！）
            yield Request(url, callback=self.parse)

    def parse(self, response):
        max_num = BeautifulSoup(response.text, 'lxml').find(
            'div', class_='pagelink').find_all('a')[-1].get_text()
        print(response.url)
        bashurl = str(response.url)[:-7]  # 对应的是start_requests中的URL
        for num in range(1, int(max_num) + 1):
            url = bashurl + '_' + str(num) + self.bashurl
            yield Request(url, callback=self.get_name)
            """
            yield Request,请求新的URL，后面是回调函数，需要哪一个函数来处理返回值，就调用那一个函数，
            返回值会以参数的形式传递给所调用的函数。
            """

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all(
            'tr', bgcolor='#FFFFFF')
        for td in tds:
            novelname = td.find('a').get_text()
            novelurl = td.find('a')['href']
            # meta字典，是Scrapy传递额外数据的方法
            yield Request(
                novelurl,
                callback=self.get_chapterurl,
                meta={'name': novelname,
                      'url': novelurl})

    def get_chapterurl(self, response):
        item = DingdianScrapyItem()
        item['name'] = str(response.meta['name']).replace(
            '\xa0', '')  # 替换空格的字符表达
        item['novelurl'] = response.meta['url']
        serialstatus = BeautifulSoup(response.text, 'lxml').find(
            'table').find_all('td')[2].get_text()
        serialnumber = BeautifulSoup(response.text, 'lxml').find(
            'table').find_all('td')[4].get_text()
        category = BeautifulSoup(response.text, 'lxml').find(
            'table').find('a').get_text()
        author = BeautifulSoup(response.text, 'lxml').find(
            'table').find_all('td')[1].get_text()
        bash_url = BeautifulSoup(response.text, 'lxml').find(
            'p', class_='btnlinks').find('a', class_='read')['href']
        name_id = str(bash_url)[-6:-1].replace('/', '')
        item['serialstatus'] = str(serialstatus).strip()
        item['serialnumber'] = str(serialnumber).strip()
        item['category'] = str(category).replace('/', '')
        item['author'] = str(author).replace('/', '').strip()
        item['name_id'] = name_id
        yield item
        yield Request(
            url=bash_url,
            callback=self.get_chapter,
            meta={'name_id': name_id})

    def get_chapter(self, response):
        urls = re.findall(
            r'<td class="L"><a href="(.*?)">(.*?)</a></td>', response.text)
        num = 0
        for url in urls:
            num += 1
            chapterurl = response.url + url[0]
            chaptername = url[1]
            rets = Sql.select_chapter(chapterurl)
            if rets[0] == 1:
                print('章节已经存在了')
                pass
            else:
                yield Request(chapterurl,
                              callback=self.get_chaptercontent,
                              meta={'num': num,
                                    'name_id': response.meta['name_id'],
                                    'chaptername': chaptername,
                                    'chapterurl': chapterurl})

    def get_chaptercontent(self, response):
        item = DcontentItem()
        item['num'] = response.meta['num']
        item['id_name'] = response.meta['name_id']
        item['chaptername'] = str(
            response.meta['chaptername']).replace('\xa0', '')
        item['chapterurl'] = response.meta['chapterurl']
        content = BeautifulSoup(response.text, 'lxml').find(
            'dd', id='contents').get_text()
        item['chaptercontent'] = str(content).replace('\xa0', '')
        return item
