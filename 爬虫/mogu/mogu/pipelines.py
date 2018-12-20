# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
client = pymongo.MongoClient('localhost', 27017)

db = client.mogu

biao = db.mogu



class MoguPipeline(object):
    def process_item(self, item, spider):
        biao.insert(dict(item))
        return item
