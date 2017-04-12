# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from .items import DyttItem, ClImg
from .settings import DYTT_COL, DYTT_MONGODB, DYTT_ZUIXIN_COL, CL_COL, CL_MONGODB


class MyscrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class DyttPipeline(object):
    def __init__(self):
        client = MongoClient()
        db = client[DYTT_MONGODB]
        self.col = db[DYTT_COL]

    def process_item(self, item, spider):
        if isinstance(item, DyttItem):
            url = item['url']
            if self.col.find_one({'url': url}):
                print('该电影已经存在了', '-' * 27)
            else:
                post = {
                    '电影天堂标题': item['title_dytt'],
                    '海报大图': item['img_url'],
                    '电影截图': item['img_url_detail'],
                    '下载链接': item['download_url'],
                    'url': item['url']
                }
                self.col.save(post)
                print('插入一条影片', '*' * 27)


class DyttZuixinPipeline(object):
    def __init__(self):
        client = MongoClient()
        db = client[DYTT_MONGODB]
        self.col = db[DYTT_ZUIXIN_COL]

    def process_item(self, item, spider):
        if isinstance(item, DyttItem):
            url = item['url']
            if self.col.find_one({'url': url}):
                print('该电影已经存在了', '-' * 27)
            else:
                post = {
                    '电影天堂标题': item['title_dytt'],
                    '海报大图': item['img_url'],
                    '下载链接': item['download_url'],
                    'url': item['url']
                }
                self.col.save(post)
                print('插入一条影片', '*' * 27)


class ClPipeline(object):
    def __init__(self):
        client = MongoClient()
        db = client[CL_MONGODB]
        self.col = db[CL_COL]

    def process_item(self, item, spider):
        if isinstance(item, ClImg):
            url = item['item_url']
            if self.col.find_one({'套图地址': url}):
                print('该套图链接已存在')
            else:
                post = {
                    '套图地址': item['item_url'],
                    '套图标题': item['title'],
                    '图片地址列表': item['img_urls'],
                    'download': item['download']
                }
                self.col.save(post)
                print('插入一个套图信息', '*' * 27, "%s" % item['title'])
