# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meinv.items import MeinvItem
from scrapy.http import Request
import requests
import os
class MnSpider(CrawlSpider):
    name = 'mn'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/']

    rules = (
        #获取所有的分类
        Rule(LinkExtractor(allow=('http://.*?/'),restrict_xpaths=('//ul[@class="menu"]/li/a'))),
        #获取页面
        Rule(LinkExtractor(allow=('.*?/page/\d+/'), restrict_xpaths=('//div[@class="nav-links"]/a')), follow=True),
        Rule(LinkExtractor(allow=('http://www.mzitu.com/\d+'), restrict_xpaths=('//ul[@id="pins"]/li/a')),callback='parse_item',),
    )

    def parse_item(self, response):
        item = MeinvItem()
        #print(response.url)
        refer = response.request.headers.getlist('Referer')
        refer = str(refer[0])[1:]
        #print(refer)
        item['headers']={
        'Referer':refer,
        'User - Agent':'Mozilla / 5.0(WindowsNT10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 55.0.2883.87Safari / 537.36',
        }

        #标题
        item['title'] = response.xpath('//h2[@class="main-title"]/text()').extract_first('')
        #分类
        item['classify'] = response.xpath('//div[@class="main-meta"]/span[1]/a/text()').extract_first('')
        #发布时间
        item['time'] = "".join(response.xpath('//div[@class="main-meta"]/span[2]/text()').extract_first('')).replace('发布于','')
        #浏览量
        item['page_view'] = response.xpath('//div[@class="main-meta"]/span[3]/text()').extract_first()
        #图片链接
        item['image_link'] = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract()
        url = item['image_link'][0]

        yield item






