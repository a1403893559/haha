# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from chian.items import ChianItem
from scrapy_redis.spiders import RedisCrawlSpider

class ChinaspiderSpider(RedisCrawlSpider):
    name = 'chinaspider'
    allowed_domains = ['china.com']
    redis_key = 'zhwSpider:start_urls'
    #start_urls = ['https://travel.china.com/hotspot/']

    rules = (
        Rule(LinkExtractor(allow=r'h.*?index_\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        item = ChianItem()
        article_list = response.xpath('//div[@class="m_Con"]')
        #print(article_list)
        for i in article_list:
            item['title'] = i.xpath('.//div[2]/h2/a/text()').extract()
            item['content'] = i.xpath('.//div[2]/div/text()').extract()
            item['time'] = i.xpath('.//div[2]/p/span/text()').extract()
            print(item['title'])
            print(item['content'])
            print(item['time'])
            yield item