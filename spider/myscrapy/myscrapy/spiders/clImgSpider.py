# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re
from ..items import ClImg


class ClimgspiderSpider(scrapy.Spider):
    name = "clImgSpider"
    allowed_domains = ["cl.y9n.pw"]
    # start_urls = ['http://cl.y9n.pw/']
    base_url = 'http://cl.y9n.pw/thread0806.php?fid=16&search=&page='

    def start_requests(self):
        for pageNum in range(1, 50):
            yield Request(self.base_url + str(pageNum), callback=self.parse_page)

    def parse_page(self, response):
        page_base_url = 'http://cl.y9n.pw/'
        all_a = response.xpath('//h3/a[@target="_blank"]/@href').extract()
        for a in all_a:
            item_url = page_base_url + a
            yield Request(item_url, callback=self.parse_item, meta={'item_url': item_url})

    def parse_item(self, response):
        item = ClImg()
        item['item_url'] = response.meta['item_url']
        item['img_urls'] = response.xpath('//input/@src').extract()
        item['title'] = response.xpath('//h4/text()').extract()[0]
        item['download'] = 0
        return item
