# -*- coding: utf-8 -*-
import scrapy
from twoci.items import TwociItem

class BanciyuanSpider(scrapy.Spider):
    name = 'banciyuan'
    allowed_domains = ['bcy.net']
    start_urls = ['https://bcy.net/circle/timeline/showtag?since=25101.527&grid_type=flow&sort=hot&tag_id=5798']

    def parse(self, response):

        item = TwociItem()
        item['name'] = response.xpath('//span[@class="fz12 lh18 username cut dib vam"]/text()').extract()
        item['like'] = response.xpath('//span[@class="like"]/text()').extract()
        item['imgurl'] = response.xpath('//img[@class="cardImage"]/@src').extract()
        item['title'] = response.xpath('//span[@class="fz12 lh18 username cut dib vam"]/text()').extract_first()
        url = response.xpath('//li[@class="js-smallCards _box"][last()]/@data-since').extract()


        pinjie = 'https://bcy.net/circle/timeline/showtag?since='+url[0]+'&grid_type=flow&sort=hot&tag_id=5798'

        yield item

        yield scrapy.Request(pinjie,callback=self.parse)