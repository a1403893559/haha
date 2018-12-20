# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
from dianying.items import ZhongguoItem,YugaoItem,HaolaiwuItem
import pymongo
class DianyingPipeline(object):
    def __init__(self,host,port,db):
        client = pymongo.MongoClient(host,port)
        self.db = client['jishi']

    @classmethod
    def from_settings(cls,settings):
        host = settings['HOST']
        port = settings['PORT']
        db = settings['DB']
        return cls(host,port,db)

    def process_item(self, item, spider):
        if isinstance(item,ZhongguoItem):
            collections = self.db['chxinwen']
            collections.insert(dict(item))


        if isinstance(item,YugaoItem):
            collections = self.db['dianying']
            collections.insert(dict(item))

        if isinstance(item, HaolaiwuItem):
            collections = self.db['haolaiwu']
            collections.insert(dict(item))

        return item
