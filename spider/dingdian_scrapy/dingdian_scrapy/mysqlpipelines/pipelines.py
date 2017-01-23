from .sql import Sql
from dingdian_scrapy.items import DingdianScrapyItem


class DingdianPipeline(object):

    def process_item(self, item, spider):
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
                Sql.insert_dd_name(
                    xs_name,
                    xs_author,
                    serialstatus,
                    serialnumber,
                    category,
                    name_id)
                print('开始存小说标题')

