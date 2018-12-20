# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeihanItem(scrapy.Item):
    content = scrapy.Field()
    author = scrapy.Field()
    laugh = scrapy.Field()
    talk = scrapy.Field()
    img = scrapy.Field()

