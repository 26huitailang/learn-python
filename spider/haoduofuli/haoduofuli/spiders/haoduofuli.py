# !/usr/bin/env python
# -*- coding: utf8 -*-
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from haoduofuli.items import HaoduofuliItem
from scrapy import FormRequest