# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from bolejob.items import *


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = []
    for i in range(1,5):
        url = 'http://blog.jobbole.com/all-posts/page/'+str(i)
        start_urls.append(url)

    def parse(self, response):
        print(response.status)
        url = response.xpath('//div[@class="post-meta"]/p[1]/a[1]/@href').extract()
        title = response.xpath('//div[@class="post-meta"]/p[1]/a[1]/text()').extract()
        for i in url:
            yield scrapy.Request(i,callback=self.parse_son)


    def parse_son(self,response):
        item = BolejobItem()
        item['url'] = response.xpath('//link[@rel="canonical"]/@href').extract()
        item['title'] = response.xpath('//title/text()').extract()
        soup = BeautifulSoup(response.text)
        date = soup.find('p',attrs={'class':'entry-meta-hide-on-mobile'}).get_text()

        item['date'] = date[16:26]
        content = response.xpath('//div[@class="entry"]/p').extract()
        nei = soup.select('.entry p')
        content = ''
        for i in nei:
            content = content + i.get_text()
        item['content'] = content

        item['like'] = response.xpath('//h10/text()').extract()
        item['shoucang'] = response.xpath('//span[@class="btn-bluet-bigger href-style bookmark-btn  register-user-only "]/text()')
        item['talk'] = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a[2]/text()').extract()
        item['biaoqian'] = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a[1]/text()').extract()
        item['pic'] = response.xpath('//div[@class="entry"]/p/img/@src').extract()


        #date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()

        # date = re.findall(r'<p class="entry-meta-hide-on-mobile">(\d+//\d+//\d+)\s<a', response.text)
        yield item
