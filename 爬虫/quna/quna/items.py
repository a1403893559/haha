# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QunaItem(scrapy.Item):
    title = scrapy.Field()
    types = scrapy.Field()
    sm = scrapy.Field()
    price = scrapy.Field()
    date = scrapy.Field()
    renshu = scrapy.Field()
    img = scrapy.Field()
    coll = scrapy.Field()
    pass
