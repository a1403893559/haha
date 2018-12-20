# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BolejobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    pic = scrapy.Field()
    like = scrapy.Field()
    shoucang = scrapy.Field()
    talk = scrapy.Field()
    content = scrapy.Field()
    biaoqian = scrapy.Field()
    imgpath = scrapy.Field()
