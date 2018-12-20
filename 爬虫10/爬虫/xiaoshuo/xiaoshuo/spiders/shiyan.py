# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import lxml

class ShiyanSpider(CrawlSpider):
    name = 'shiyan'
    allowed_domains = ['qisuu.la']
    start_urls = ['https://www.qisuu.la/soft/sort01/']


    rules = (
        # Rule(LinkExtractor(allow=('/soft/sort\d+/'),
        #                    restrict_xpaths=('//div[@class="nav"]/a')), follow=True),


        Rule(LinkExtractor(allow=("/.*?/.*?\d+/index_\d+.html"),
                           )),

        Rule(LinkExtractor(allow=('/du/\d+/\d+/'),
                           restrict_xpaths=('//div/a')),callback='mulu'),

        Rule(LinkExtractor(allow=('\d+.html')),
                            callback='content1'),


    )

    def parse_item(self, response):
        zz = re.compile(r"页次：\d+/\d+")
        rr = re.findall(zz,response.text)
        # print(rr)
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
    def mulu(self,response):

        a = response.xpath('//div[@class="pc_list"]/ul/li/a/@href').extract()
        a = a[12:]
        print('')

    def content1(self,response):
        print(response.text)