# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DyttItem(scrapy.Item):
    # 电影天堂
    url = scrapy.Field()
    time_dytt = scrapy.Field()
    time_movie = scrapy.Field()
    title_dytt = scrapy.Field()
    title_en = scrapy.Field()
    img_url = scrapy.Field()
    img_url_detail = scrapy.Field()
    imdb = scrapy.Field()
    download_url = scrapy.Field()


class TorrentItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    size = scrapy.Field()


class Article(scrapy.Item):
    title = scrapy.Field()


class ClImg(Item):
    item_url = Field()
    title = Field()
    img_urls = Field()
    download = Field() # 0 没有 1 完成


