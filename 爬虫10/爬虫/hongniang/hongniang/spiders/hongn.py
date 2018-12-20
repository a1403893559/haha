# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hongniang.items import *
from scrapy_redis.spiders import RedisCrawlSpider

class HongnSpider(RedisCrawlSpider):
    name = 'hongn'
    allowed_domains = ['hongniang.com']
    redis_key = 'hongn:start_urls'
    # start_urls = ['http://www.hongniang.com/index/search?sort=0&wh=0&sex=2&starage=1,2,3,4,5,6,7,8,9,10&province=0&city=0&marriage=1&edu=3,2,4,5,6,7&income=1,2,3,4,5,6,7,8&height=0&pro=0&house=0&child=0&xz=0&sx=0&mz=0&hometownprovince=0']
    rules = (
        Rule(LinkExtractor(allow=r'http.*?page=\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='.*?user.*?',allow_domains='www.hongniang.com'), callback='parse_detail', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
    def parse_detail(self, response):

        item = HongniangItem()
        item['name'] = response.xpath('//div[@class="name nickname"]/text()').extract()[0].strip()
        item['age'] = response.xpath('//div[@class = "sub1"]//div[@class="info2"]//ul[1]/li[1]/text()').extract()
        item['height'] = response.xpath('//div[@class = "sub1"]//div[@class="info2"]//ul[2]/li[1]/text()').extract()
        item['workadd'] = response.xpath('//div[@class = "sub1"]//div[@class="info2"]//ul[3]/li[2]/text()').extract()

        yield item