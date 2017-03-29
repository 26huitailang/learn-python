# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import TorrentItem


class MininovaSpider(CrawlSpider):
    name = "mininova"
    allowed_domains = ["mininova.org"]
    start_urls = (
        'http://www.mininova.org/',
    )
    rules = [Rule(LinkExtractor('/tor/\d+'), callback="parse_torrent")]

    def parse_torrent(self, response):
        torrent = TorrentItem()
        torrent['url'] = response.url
        torrent['name'] = response.xpath("//h1/text()").extract()
        torrent['description'] = response.xpath("//div[@id='description']").extract()
        torrent['size'] = response.xpath("//div[@id='specifications']/p[2]/text()[2]").extract()
        print(torrent)
        return torrent
