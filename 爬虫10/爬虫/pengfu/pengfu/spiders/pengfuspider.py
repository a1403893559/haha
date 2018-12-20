# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pengfu.items import *



class PengfuspiderSpider(CrawlSpider):
    name = 'pengfuspider'
    allowed_domains = ['www.pengfu.com']    #允许爬取的域
    start_urls = ['http://www.pengfu.com/']  #起始url

    rules = (   #根据正则匹配一层一层的找想要爬取的数据
        Rule(LinkExtractor(allow=r'https://www.pengfu.com/.*?1.html',restrict_xpaths='//ul[@class="clearfix"]/li/a'), callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=r'https://www.pengfu.com/.*?_\d+.html', restrict_xpaths='//div[@class="page"]/div/a'),
             callback='parse_page', follow=True),
        Rule(LinkExtractor(allow=r'.*?/.*?_\d+_\d+.html',restrict_xpaths='//h1[@class="dp-b"]/a'),
             callback='parse_content'),


    )

    def parse_item(self, response):

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        print('')
    def parse_page(self,response):
        print('')
    def parse_content(self, response):
        item = PengfuItem()
        content = response.xpath('//div[@class="content-txt pt10"]/text()').extract()  #这是内容
        title = response.xpath('//div[@class="list-item bg1 b1 boxshadow"]/dl/dd/h1/text()').extract()
#这是标题
        item['img'] = response.xpath('//div[@class="content-txt pt10"]/img/@src|//div[@class="content-txt pt10"]/p/img/@src').extract()
        item['name'] = response.xpath('//div[@class= "list-item bg1 b1 boxshadow"]/dl/dd/p/a/text()').extract()
#这是图片地址,和作者名字
        text = ''.join(content)      #爬下来的内容发现有一堆换行符,要把它替换掉
        text = text.replace('\t','')
        text = text.replace('\n','')
        title = title[0].replace('\t','')
        print(text)
        item['text'] = text
        item['title'] =  title
        yield item   #返回数据
