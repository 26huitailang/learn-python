#!/usr/bin/python
# coding: utf-8

import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request  # 跟进URL的时候用
from dingdian_scrapy.items import DingdianScrapyItem, DcontentItem
from dingdian_scrapy.mysqlpipelines.sql import Sql


class Myspider(scrapy.Spider):
    """
    定义爬虫方法的类，继承自scrapy.Spider类
    start_requests
    parse
    get_name
    get_chapterurl
    get_chaptercontent
    """
    name = 'dingdian'  # entrypoint.py中的对应的第三个参数，此名字整个项目有且只能有一个
    allowed_domains = ['23us.com']  # 爬取规则，只会跟进存在于此的URL
    bash_url = 'http://www.23us.com/class/'  # 分类的基本url
    bashurl = '.html'  # url拼接使用

    def start_requests(self):
        """
        拼接发现的小说分类的URL
        散文诗词：http://www.23wx.com/class/9_1.html
        用yield将函数变为生成器，每次返回一个可迭代的对象
        Request使用回调函数，将请求的response作为参数传递给self.parse
        """
        for i in range(1, 11):
            # 遍历拼接URL
            url = self.bash_url + str(i) + '_1' + self.bashurl
            # 使用Request包，跟进URL（返回的response作为参数传递给self.parse, 这个叫回调函数！）
            yield Request(url, callback=self.parse)

    def parse(self, response):
        """
        提取最大分页，拼接遍历的URL，遍历该类型的所有分页
        回调处理response获取小说名字
        """
        # 提取最大分页
        max_num = BeautifulSoup(response.text, 'lxml').find(
            'div', class_='pagelink').find_all('a')[-1].get_text()
        # 打印response的URL
        print(response.url)
        # 对应的时start_requests方法中拼接的URL，截至倒数第七位
        # http://www.23wx.com/class/9(_1.html)
        bashurl = str(response.url)[:-7]
        # 遍历所有的页面
        for num in range(1, int(max_num) + 1):
            url = bashurl + '_' + str(num) + self.bashurl
            yield Request(url, callback=self.get_name)
            """
          yield Request,请求新的URL，后面是回调函数，
          需要哪一个函数来处理返回值，就调用那一个函数，
          返回值会以参数的形式传递给所调用的函数。
          """

    def get_name(self, response):
        """
        提取小说的名字和链接，并传入self.get_chapterurl
        通过meta字典传递Scrapy的额外数据
        """
        # bs提取所有的属性符合的tr标签
        tds = BeautifulSoup(response.text, 'lxml').find_all(
            'tr', bgcolor='#FFFFFF')
        # 遍历标签获取小说的name和url
        for td in tds:
            novelname = td.find('a').get_text()
            novelurl = td.find('a')['href']
            # meta字典，是Scrapy传递额外数据的方法
            yield Request(novelurl,
                          callback=self.get_chapterurl,
                          meta={'name': novelname, 'url': novelurl})

    def get_chapterurl(self, response):
        """
        将请求获得的数据都存入DingdianScrapyItem的实例中，并返回一个iterable的item用于pipelines
        请求章节列表的地址，交由self.get_chapter处理
        """
        # 实例化DingdianScrapyItem()类，事先定义好的数据模型
        item = DingdianScrapyItem()
        # 替换空格的字符表达，并存入item的name字段
        item['name'] = str(response.meta['name']).replace(
            '\xa0', '')
        # 将数据存入item对应的字段
        item['novelurl'] = response.meta['url']
        # 提取小说的连载状态
        serialstatus = BeautifulSoup(response.text, 'lxml').find(
            'table').find_all('td')[2].get_text()
        # 提取小说目前的连载字数
        serialnumber = BeautifulSoup(response.text, 'lxml').find(
            'table').find_all('td')[4].get_text()
        # 提取小说的类型
        category = BeautifulSoup(response.text, 'lxml').find(
            'table').find('a').get_text()
        # 提取小说的作者
        author = BeautifulSoup(response.text, 'lxml').find(
            'table').find_all('td')[1].get_text()
        # 提取小说的阅读地址（所有的章节）
        bash_url = BeautifulSoup(response.text, 'lxml').find(
            'p', class_='btnlinks').find('a', class_='read')['href']
        # 获取小说的编号
        name_id = str(bash_url)[-6:-1].replace('/', '')
        # 将数据存入item对应的字段
        item['serialstatus'] = str(serialstatus).strip()
        item['serialnumber'] = str(serialnumber).strip()
        item['category'] = str(category).replace('/', '')
        item['author'] = str(author).replace('/', '').strip()
        item['name_id'] = name_id
        # DingdianScrapyItem结构的数据都已获取，返回一个item的可迭代对象iterable，用于pipelines，并继续执行
        yield item
        # 请求章节列表的地址，response由self.get_chapter处理
        yield Request(
            url=bash_url,
            callback=self.get_chapter,
            meta={'name_id': name_id})

    def get_chapter(self, response):
        """
        正则获取所有的章节地址和名字
        遍历结果，并根据数据库去重
        不存在则继续请求章节内容
        """
        # 正则表达式提取每个章节的URL
        urls = re.findall(
            r'<td class="L"><a href="(.*?)">(.*?)</a></td>', response.text)
        # scrapy是异步的，所以用自己的计数器来保持小说章节的顺序
        num = 0
        # 遍历正则结果的group
        for url in urls:
            num += 1
            # 获取的url[0]为章节的id.html格式，需拼接完整的URL
            chapterurl = response.url + url[0]
            # url[1]第二个数据为chaptername
            chaptername = url[1]
            # 根据数据库判定chapterurl是否存在
            rets = Sql.select_chapter(chapterurl)
            # 若结果为1则已经存在
            if rets[0] == 1:
                print('章节已经存在了')
                pass
            # 否则继续请求章节的内容
            else:
                yield Request(chapterurl,
                              callback=self.get_chaptercontent,
                              meta={'num': num,
                                    'name_id': response.meta['name_id'],
                                    'chaptername': chaptername,
                                    'chapterurl': chapterurl})

    def get_chaptercontent(self, response):
        """
        实例DcontentItem，用于存放章节相关的信息及内容
        直接return结果，一次完整的过程完成返回最终结果，用于pipelines
        """
        # 定义的另外一个scrapy数据结构DcontentItem用于存放章节内容及相关信息
        item = DcontentItem()
        # 章节的计数器结果
        item['num'] = response.meta['num']
        # 还是小说编号，非章节编号
        item['id_name'] = response.meta['name_id']
        # 章节名字
        item['chaptername'] = str(
            response.meta['chaptername']).replace('\xa0', '')
        # 章节地址
        item['chapterurl'] = response.meta['chapterurl']
        # 提取章节内容
        content = BeautifulSoup(response.text, 'lxml').find(
            'dd', id='contents').get_text()
        item['chaptercontent'] = str(content).replace('\xa0', '')
        # 返回类型为DcontentItem类型的item，不需要yield，某一次完成的章节内容获取完成
        return item
