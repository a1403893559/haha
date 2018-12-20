# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class PengfuPipeline(object):
    def process_item(self, item, spider):
        client = pymongo.MongoClient('localhost', 27017)   #这是保存到mongodb数据库
        db = client.pengfu
        biao = db.pengfu
        biao.insert(dict(item))
