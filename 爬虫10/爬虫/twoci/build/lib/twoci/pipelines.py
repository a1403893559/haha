# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import scrapy
import os
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import *

class bancileimg(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')
    def get_media_requests(self, item, info):
        #根据图片链接否早一个request，给调度器，放在任务队列里

        img_url = item['imgurl']
        print('哈哈')
        for i in img_url:
            yield scrapy.Request(i)


    def item_completed(self, results, item, info):
        #图片任务下载完成之后会执行这个方法

        for ok,value in  results:
            if ok:
                #return value
                image_path = value['path']

                os.rename(self.IMAGES_STORE + '/' + image_path, self.IMAGES_STORE + '/' + item['title'] + '.jpg')
                item['picurl'] = self.IMAGES_STORE + '/' + item['title'] + '.jpg'



                return item
            else:
                print('的撒多')




class TwociPipeline(object):
    def process_item(self, item, spider):
        client = pymongo.MongoClient('localhost', 27017)
        db = client.banci
        sifeizhai = db.banci
        sifeizhai.insert(dict(item))



