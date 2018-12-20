# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhongguoItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    img = scrapy.Field()
    content = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()


class YugaoItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    datelong = scrapy.Field()
    img = scrapy.Field()


class HaolaiwuItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    img = scrapy.Field()
    content = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()

