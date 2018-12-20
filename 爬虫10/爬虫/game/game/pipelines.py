# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client.game
col = db.game

class GamePipeline(object):
    def process_item(self, item, spider):
        col.insert(dict(item))
        return item
