# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.pipelines.images import *
import scrapy
import os
import pymongo
clice = pymongo.MongoClient('localhost',27017)
db = clice.baidu
co = db.co
IMAGES_STORE = get_project_settings().get('IMAGES_STORE')
class baiduimg(ImagesPipeline):

    def get_media_requests(self, item, info):
        #根据图片链接否早一个request，给调度器，放在任务队列里

        img_url = item['imgurl']
        print('哈哈')

        yield scrapy.Request(img_url)


    #def item_completed(self, results, item, info):
        #图片任务下载完成之后会执行这个方法

        #for ok,value in results:
            #if ok:
                #return value
                #image_path = value['path']
                #os.rename(IMAGES_STORE + '/' + image_path,IMAGES_STORE + '/' + item['title'] + '.jpg')
                #item['bendiimgurl'] = self.IMAGES_STORE + '/' + item['title'] + '.jpg'


        #return item






class BaidulPipeline(object):
    def process_item(self, item, spider):
        co.insert(dict(item))
        return item
