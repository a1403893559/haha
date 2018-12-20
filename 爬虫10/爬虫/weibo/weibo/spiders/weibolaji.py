# -*- coding: utf-8 -*-
import scrapy
import json
from lxml import etree
from weibo.items import WeiboItem

class WeibolajiSpider(scrapy.Spider):
    name = 'weibolaji'
    allowed_domains = ['weibo.com']
    start_urls = ['https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=1760&page=1','https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=novelty&page=1','https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=7&page=1']

    def parse(self, response):
        item = WeiboItem()
        #print(response.body)
        div = json.loads(response.body)
        item['obj'] = div
        yield item
        # dx = obj.xpath('//div[@class="UG_list_b"]')
        #
        # title = dx.xpath('//div[@class="UG_list_b"]/div[2]/h3/a/text()')
        # uname = dx.xpath('//div[@class="UG_list_b"]/div[2]/div/a[2]/span/text()')
        # print(title)
        # print(uname)

