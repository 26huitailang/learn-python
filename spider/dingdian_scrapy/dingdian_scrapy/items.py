# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 小说名字
    author = scrapy.Field()  # 作者
    novelurl = scrapy.Field()  # 小说地址
    serialstatus = scrapy.Field()  # 连载状态
    serialnumber = scrapy.Field()  # 连载字数
    category = scrapy.Field()  # 分类
    name_id = scrapy.Field()  # 小说ID


class DcontentItem(scrapy.Item):

    id_name = scrapy.Field()  # 小说编号
    chaptercontent = scrapy.Field()  # 章节内容
    num = scrapy.Field()  # 用于保持异步中章节的顺序
    chapterurl = scrapy.Field()  # 章节地址
    chaptername = scrapy.Field()  # 章节名字
