# coding=utf-8
from .sql import Sql
from dingdian_scrapy.items import DingdianScrapyItem
from dingdian_scrapy.items import DcontentItem


class DingdianPipeline(object):
    """
    process_item:判定item类型，调用sql中定义的方法插入数据
    """
    def process_item(self, item, spider):
        """
        处理item，决定数据存入数据库
        :param item:items.py中定义的数据结构的实例
        :param spider:爬虫
        :return:
        """
        if isinstance(item, DingdianScrapyItem):
            name_id = item['name_id']
            ret = Sql.select_name(name_id)
            if ret[0] == 1:
                print('已经存在了')
                pass
            else:
                xs_name = item['name']
                xs_author = item['author']
                serialstatus = item['serialstatus']
                serialnumber = item['serialnumber']
                category = item['category']
                Sql.insert_dd_name(xs_name,
                                   xs_author,
                                   serialstatus,
                                   serialnumber,
                                   category,
                                   name_id)
                print('开始存小说标题')
        if isinstance(item, DcontentItem):
            url = item['chapterurl']
            name_id = item['id_name']
            num_id = item['num']
            xs_chaptername = item['chaptername']
            xs_content = item['chaptercontent']
            Sql.insert_dd_chaptername(xs_chaptername,
                                      xs_content,
                                      name_id,
                                      num_id,
                                      url)
            print('小说存储完毕！')
            return item