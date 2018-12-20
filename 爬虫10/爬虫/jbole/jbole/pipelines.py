# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class JbolePipeline(object):
    def process_item(self, item, spider):

        with open('job.json','a') as f:
            jsonfile = json.dumps(dict(item),ensure_ascii=False)
            f.write(jsonfile)


        return item
