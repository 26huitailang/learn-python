# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from urllib import parse
from scrapy.http import Request
from ..items import DyttItem


class DyttSpider(scrapy.Spider):
    name = "dytt_zuixin"
    allowed_domains = ["dytt8.net"]
    base_url = "http://www.dytt8.net"
    start_urls = (
        'http://www.dytt8.net/index.htm',
    )

    def parse(self, response):
        zuixin_all_a = BeautifulSoup(response.text, 'lxml').find_all('div', class_='co_content8')[0].find_all('a')
        # print(zxdy_all_a)
        for a in zuixin_all_a:
            if a.get_text() == '最新电影下载':
                continue
            else:
                print("获取" + a.get_text())
                url = self.base_url + a['href']
                yield Request(url, callback=self.parse_item, meta={'title': a.get_text()})

    def parse_item(self, response):
        item = DyttItem()
        item['title_dytt'] = response.meta['title']
        item['img_url'] = BeautifulSoup(response.text, 'lxml').find_all('img')[1]['src']
        item['download_url'] = BeautifulSoup(response.text, 'lxml').find('td', bgcolor='#fdfddf').find('a')['href']
        item['url'] = response.url
        return item
