# -*- coding: utf-8 -*-
import scrapy
import re
from lxml import etree
import json
import os
from quna.items import QunaItem
rr = 0
ii = 0
oo = 0

class QuspiderSpider(scrapy.Spider):
    name = 'quspider'
    allowed_domains = ['qunar.com']

    start_urls = ['https://tuan.qunar.com/vc/index.php?category=all_r&limit=0%2C30','https://tuan.qunar.com/vc/index.php?category=all_i&limit=0%2C30','https://tuan.qunar.com/vc/index.php?category=all_o&limit=0%2C30']

    def parse(self, response):
        item = QunaItem()
        #print(response.url[49:50])
        #print(response.text)

        zz = re.compile(r'<script>(.*?)</script>',re.S)

        html = re.findall(zz,response.text)[6][11:-2]
        html = json.loads(html)['html'][1:]
        html = etree.HTML(html)

        title = html.xpath('//div[@class="nm"]/@title')
        types = html.xpath('//div[@class="type_gt"]/text()')
        sm = html.xpath('//div[@class="sm"]/@title')
        price = html.xpath('//span[@class="cash"]/em/text()')
        date = html.xpath('//span[@class="time png24 tuan-date"]/text()')
        renshu = html.xpath('//span[@class="buy png24"]/text()')
        img = html.xpath('//div[@class="imgs loading"]/img/@data-lazy')
        coll = 'zzh' + response.url[49:50]
        if title == []:
            pass

        for i in title:
            sy = title.index(i)
            item['title'] = i
            item['types'] = types[int(sy)]
            item['sm'] = sm[int(sy)]
            item['price'] = price[int(sy)]
            item['date'] = date[int(sy)]
            item['renshu'] = renshu[int(sy)]
            item['img'] = img[int(sy)]
            item['coll'] = coll
            yield item
        url_type = re.findall('.*?category=(.*?_.?)', response.url)[0]
        url_page = int(re.findall('.*?limit=(\d+).*?', response.url)[0]) + 30
        url = 'https://tuan.qunar.com/vc/index.php?category=%s&limit=%d,30' % (url_type,url_page)
        yield scrapy.Request(url,callback=self.parse)





