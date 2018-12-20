# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
import re
from jbole.items import JboleItem
class JbspiderSpider(scrapy.Spider):
    name = 'jbspider'
    allowed_domains = ['http://blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        item = JboleItem()
        title = response.xpath('//a[@class="archive-title"]/text()').extract()


        date1 = response.xpath('//div[@class="post floated-thumb"]/div[@class="post-meta"]/p[1]/text()').re('\d+/\d+/\d+',re.S)
        zz2 = re.compile(r'<span.*?"excerpt"><p>(.*?).*?</span>',re.S)


        content = re.findall(zz2,response.text)
        types = response.css('.post .post-meta p').xpath('a[2]/text()').extract()
        img = response.xpath('//div[@class="post floated-thumb"]/div[@class="post-thumb"]/a/img/@src').extract()

        url = response.xpath('//a[@class="next page-numbers"]/@href').extract()
        print(date1)
        print(len(date1))
        for i in title:
            sy = title.index(i)
            item['title'] = i
            item['date'] = date1[int(sy)]
            item['content'] = content[int(sy)]
            item['types'] = types[int(sy)]
            item['img'] = img[int(sy)]
            yield item




        yield scrapy.Request(url=url[0],callback=self.parse,dont_filter=True)





        pass
