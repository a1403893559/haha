# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class JishiPipeline(object):
    def process_item(self, item, spider):
        client = pymongo.MongoClient('localhost', 27017)
        db = client.baidulvyou_zzh
        sifeizhai = db.lvyou_zzh
        sifeizhai.insert(dict(item))
        return item
