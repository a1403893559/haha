# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeinvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()



    # 标题
    title = scrapy.Field()
    #分类
    classify = scrapy.Field()
    #发布时间
    time = scrapy.Field()
    #浏览量
    page_view = scrapy.Field()
    #图片链接
    image_link = scrapy.Field()

    path = scrapy.Field()

    headers = scrapy.Field()