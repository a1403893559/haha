# -*- coding: utf-8 -*-
import scrapy
from dianying.items import HaolaiwuItem,YugaoItem,ZhongguoItem

class DianSpider(scrapy.Spider):
    name = 'dian'
    allowed_domains = ['1905.com']
    start_urls = ['http://www.1905.com/film/filmnews/ch/','http://www.1905.com/film/filmnews/ea/','http://www.1905.com/video/search/lst/t158e1d0o2p1.html']
    #start_urls = ['http://www.1905.com/video/search/lst/t158e1d0o2p1.html']
    def parse(self, response):

        if response.url[34:36] == 'ch':
            item = ZhongguoItem()
            div = response.css('ul.pic-event-over li.pic-pack-out')
            for i in div:
                item['title'] = i.css('.pic-pack-inner h3 a ::attr(title)').extract_first('')
                item['href'] = i.css('.pic-pack-inner h3 a ::attr(href)').extract_first('')
                item['content'] = i.css('.pic-pack-inner p ::text').extract_first('')
                item['img'] = i.css('a img ::attr(src)').extract_first('')
                item['date'] = i.css('div.pic-pack-inner div.clear span ::text').extract_first('')
                item['name'] = ','.join(i.css('div.pic-pack-inner div.clear a ::text').extract())
                yield item
            url = response.xpath('//a[@class="next"]/@href').extract()

            if len(url) !=0:
                yield scrapy.Request(url[0],callback=self.parse)
        elif response.url[34:36] == 'ea':
            item = HaolaiwuItem()
            div = response.css('ul.pic-event-over li.pic-pack-out')
            for i in div:
                item['title'] = i.css('.pic-pack-inner h3 a ::attr(title)').extract_first('')
                item['href'] = i.css('.pic-pack-inner h3 a ::attr(href)').extract_first('')
                item['content'] = i.css('.pic-pack-inner p ::text').extract_first('')
                item['img'] = i.css('a img ::attr(src)').extract_first('')
                item['date'] = i.css('div.pic-pack-inner div.clear span ::text').extract_first('')
                item['name'] = ','.join(i.css('div.pic-pack-inner div.clear a ::text').extract())
                yield item
            url = response.xpath('//a[@class="next"]/@href').extract()

            if len(url) !=0:
                yield scrapy.Request(url[0],callback=self.parse)
        elif response.url[20:25] == 'video':
            li = response.css('ul.listCon li')
            item = YugaoItem()
            for i in li:
                item['title'] = i.css('h3 a ::text').extract_first('')
                item['href'] = i.css('h3 a ::attr(href)').extract_first('')
                item['datelong'] = i.css('div a span.txt span ::text').extract_first('')
                item['img'] = i.css('div a img ::attr(src)').extract_first('')
                yield item
            url = response.xpath('//a[@class="next"]/@href').extract()

            if len(url) != 0:
                yield scrapy.Request(url[0],callback=self.parse)
