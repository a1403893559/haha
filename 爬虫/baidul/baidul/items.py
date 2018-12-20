# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidulItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content= scrapy.Field()
    user= scrapy.Field()
    zan= scrapy.Field()
    eyes= scrapy.Field()
    count= scrapy.Field()
    huifu= scrapy.Field()
    imgurl = scrapy.Field()
    userurl = scrapy.Field()
    bendiimgurl = scrapy.Field()
    pass
