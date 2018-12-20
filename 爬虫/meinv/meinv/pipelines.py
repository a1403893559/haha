# -*- coding: utf-8 -*-
import scrapy
import os
import pymongo
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
#Define your item pipelines here

#Don't forget to add your pipeline to the ITEM_PIPELINES setting
#See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
class MeinvImagePipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):

        image_url = item['image_link'][0]
        print(image_url)
        yield scrapy.Request(image_url,headers=item['headers'])
    def item_completed(self, results, item, info):
        for ok,value in results:
            if ok:
                image_path = value['path']
                os.rename(self.IMAGES_STORE + '/' + image_path,self.IMAGES_STORE + '/' + item['title'] + '.jpg')
                item['path'] = self.IMAGES_STORE + '/' + item['title'] + 'jpg'
                return item


class MeinvPipeline(object):
    # def __init__(self):
    #     self.file = open('imageurl.json', 'a+')

    def process_item(self, item, spider):
        pass
        #print(item)
    #     data = json.dumps(dict(item), ensure_ascii=False)
    #     self.file.write(data + '\n')
        #return item
    #
    # def close_spider(self, spider):
    #     self.file.close()






# def __init__(self):
    #     self.client = pymongo.MongoClient('localhost', 27017)
    #     db = self.client.meinv
    #     self.mm = db.mn
    #
    # def open_spider(self, spider):
    #     print('开始了')
    #
    # def process_item(self, item, spider):
    #     self.mm.insert(dict(item))
    #     print(self.mm)
    #     return item
    #
    # def close_spider(self, spider):
    #     self.client.close()
    #     print('结束了')