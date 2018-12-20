# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JboleItem(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    content = scrapy.Field()
    types = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()

