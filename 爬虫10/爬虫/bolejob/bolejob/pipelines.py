# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.pipelines.images import *
import scrapy

class jobboleimg(ImagesPipeline):
    def get_media_requests(self, item, info):
        #根据图片链接否早一个request，给调度器，放在任务队列里
        img_url = item['pic']
        yield scrapy.Request(img_url[0])


    def item_completed(self, results, item, info):
        #图片任务下载完成之后会执行这个方法
        for ok,value in  results:
            if ok:
                #return value
                image_path = value['path']
                item['imgpath'] = image_path
                return item

class BolejobPipeline(object):
    def process_item(self, item, spider):
        client = pymongo.MongoClient('localhost', 27017)
        db = client.bole
        wenzhang = db.wenzhang
        wenzhang.insert(dict(item))
        print(item)
        return item

