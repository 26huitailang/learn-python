#!/usr/bin/python
# coding: utf-8
from datetime import datetime, timedelta
from pymongo import MongoClient, errors


class MongoQueue:

    OUTSTANDING = 1  # 初始状态
    PROCESSING = 2
    COMPLETE = 3

    def __init__(self, db, collection, timeout=300):
        self.client = MongoClient()
        self.Client = self.client[db]
        self.db = self.Client[collection]
        self.timeout = timeout

    def __bool__(self):
        record = self.db.find_one(
            {'status': {'$ne': self.COMPLETE}}
        )
        return True if record else False

    def push(self, url, title):
        try:
            self.db.insert({'_id': url, 'status': self.OUTSTANDING, '主题': title})
            print(url, '插入队列成功')
        except errors.DuplicateKeyError as e:
            print(url, '已经存在与队列中了')
            pass

    def push_imgurl(self, title, url):
        try:
            self.db.insert({'_id': title, 'status': self.OUTSTANDING, 'url': url})
            print('图片地址插入成功')
        except errors.DuplicateKeyError as e:
            print('地址已经存在了')
            pass

    def pop(self):
        record = self.db.find_and_modify(query={'status': self.OUTSTANDING},
                                         update={'$set': {'status': self.PROCESSING, 'timestamp': datetime.now()}})
        if record:
            return record['_id']
        else:
            self.repair()
            raise KeyError

    def pop_title(self, url):
        record = self.db.find_one({'_id': url})
        return record['主题']

    def peek(self):
        record = self.db.find_one({'status': self.OUTSTANDING})
        if record:
            return record['_id']

    def complete(self, url):
        self.db.update({'_id': url},
                       {'$set': {'status': self.COMPLETE}}
                       )

    def repair(self):
        # timeout且没有COMPLETE的文档，将状态更新为OUTSTANDING
        record = self.db.find_and_modify(
            query={
                'timestamp': {'$lt': datetime.now() - timedelta(seconds=self.timeout)},  # less than
                'status': {'$ne': self.COMPLETE}  # not equal
            },
            update={'$set': {'status': self.OUTSTANDING}}
        )
        if record:
            print('重置URL状态', record['_id'])

    def clear(self):
        """
        只有第一次才调用，后续不要调用，删除数据库！
        """
        self.db.drop()
