# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from scrapy.http import Request
from jishi.items import *


class JishispiderSpider(CrawlSpider):


    name = 'jishispider'
    allowed_domains = ['lvyou.baidu.com']
    start_urls = ['https://lvyou.baidu.com/scene/t-all_s-all_a-all_l-all']

    rules = (
        Rule(LinkExtractor(allow=r'.rn=\d+&pn=\d+',),
             follow=True),
        Rule(LinkExtractor(allow=r'/.*?/',restrict_xpaths=('//li[@class="mod-view"]/a[@class="nslog"]')), callback='parse_item',follow=True),


    )

    def parse_item(self, response):

        item = JishiItem()
        item['title'] = response.xpath('//a[@class="clearfix"]/text()').extract_first('')
        item['fen']  = response.xpath('//div[@class="main-score"]/text()').extract_first('').replace('\n','')
        item['content'] = response.xpath('//p[@class="main-desc-p"]/text()').extract_first('').replace('\n','')
        lajiurl = response.xpath('//*[@id="J_line-more-href"]/@href').extract()
        item['dianping'] = response.css('.remark-count ::text').re('\d+条点评')[0]
        item['jijie'] = response.css('.main-besttime span::text')[0].extract().replace('\n','')
        item['meitu'] = 'https://lvyou.baidu.com'+response.css('.pic-count a::attr(href)')[0].extract()
        pingluntime = response.css('.ri-time::text')[0].extract().replace('\n','')
        pinglunname = response.css('.ri-uname::text')[0].extract()
        pingluncontent = response.css('.ri-remarktxt::text')[0].extract().replace('\n','')
        youyong  = response.css('.ri-dig-available span::text')[0].extract()
        huifu = response.css('.ri-comment span::text')[0].extract()
        item['pinglun'] = {'pingluntime':pingluntime,'pinglunname':pinglunname,'pingluncontent':pingluncontent,'youyong':youyong,'huifu':huifu}

        for i in lajiurl:
            url = 'https://lvyou.baidu.com'+i
            yield Request(url=url,callback=self.parse_detail,meta={'item':item})


    def parse_detail(self,response):
        item = response.meta['item']
        bigdiv = response.css('.counselor-plan-detail')
        item['url'] = response.xpath('//a[@class="plan-flayer"]/@href').extract()
        luxianlist = []
        for i in bigdiv:
            xctitle = i.css('.plan-title::text').extract_first('')
            luxian = i.css('.day-dest span::text').extract()
            jinbujin = i.css('.key-word span ::text').extract()
            if jinbujin == []:
                jincou = ','.join(jinbujin)
            else:
                jincou = '无'
            luxianlist.append(dict({xctitle:[{'路线':'->->'.join(luxian),'行程':jincou}]}))
        item['luxian'] = luxianlist

        return item





