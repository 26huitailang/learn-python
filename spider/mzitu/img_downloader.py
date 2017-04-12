# coding: utf-8
from pymongo import MongoClient
from .download import request

class ImgDownloader(object):

    def __init__(self):
        client = MongoClient()
        db = client['cl']
        self.col = db['climg']
        self.url_list = []
        self.title = []

    def get_item(self):
        item = self.col.find_one_and_update({'download': 0},{'$inc':{'download': 1}} )
        return item

    def mkdir(self, item):
        pass

if __name__ == '__main__':
    downloader = ImgDownloader()
    downloader.get_item()