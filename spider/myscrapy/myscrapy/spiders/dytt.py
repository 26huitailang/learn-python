# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy.http import Request
from ..items import DyttItem


class DyttSpider(scrapy.Spider):
    name = "dytt"
    allowed_domains = ["ygdy8.net"]
    base_url = "http://www.ygdy8.net/html/gndy/dyzz/"
    start_urls = (
        'http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html',
    )

    def parse(self, response):
        next_selector = response.xpath('//select[@name="sldd"]//option/@value')
        for page in next_selector.extract():
            yield Request(parse.urljoin(self.base_url, page), callback=self.parse)

        item_selector = response.xpath('//a[@class="ulink"]/@href')
        for item in item_selector.extract():
            yield Request(parse.urljoin(self.base_url[:-15], item), callback=self.parse_item)

    def parse_item(self, response):
        item = DyttItem()
        item['title_dytt'] = response.xpath('//div[@class="title_all"]//font/text()').extract()
        item['img_url'] = response.xpath('//div[@id="Zoom"]//img[1]/@src').extract()
        item['img_url_detail'] = response.xpath('//div[@id="Zoom"]//img[2]/@src').extract()
        item['download_url'] = response.xpath('//td[@bgcolor="#fdfddf"]/a/text()').extract()
        item['url'] = response.url
        return item
