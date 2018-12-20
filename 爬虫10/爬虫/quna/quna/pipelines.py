# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.utils.project import get_project_settings

class QunaPipeline(object):
    def __init__(self,cliect,dbs):
        self.cliect = cliect
        self.dbs = dbs


    @classmethod
    def from_settings(cls,settings):
        host = settings['HOST']
        port = settings['PORT']
        db = settings['DB']
        cliect = pymongo.MongoClient(host,port)
        dbs = cliect[db]
        return cls(cliect,dbs)

    def process_item(self, item, spider):
        col = self.dbs[item['coll']]
        col.insert(dict(item))