# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JishiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    fen = scrapy.Field()
    url = scrapy.Field()
    luxian = scrapy.Field()
    jijie = scrapy.Field()
    dianping = scrapy.Field()
    meitu = scrapy.Field()
    pinglun = scrapy.Field()