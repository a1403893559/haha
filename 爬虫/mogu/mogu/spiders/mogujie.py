# -*- coding: utf-8 -*-
import scrapy
import json
import re
idlist = []
leilist = []
from mogu.items import MoguItem


class MogujieSpider(scrapy.Spider):
    name = 'mogujie'
    allowed_domains = ['.']
    start_urls = ['http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery211019971151140352905_1532589442489&pids=110119&appPlat=pc&_=1532589442490']

    def parse(self, response):

        a = json.loads(response.text[42:-1])['data']['110119']['list']  # 切割返回的字符 # 利用json改变他变成字典
        #print(a)# 字典取值，一层一层的取
        for i in a:  # 取出来的字典的值是一个列表
            idlist.append(i["categoryDetailPid"])
            leilist.append(i["categoryName"])
        #print(idlist)
        for i in idlist:
            url = 'http://mce.mogujie.com/jsonp/makeup/3?token=WPNdZevFbj4azNu7OqMLfXcF1RPfTRnjbC65UDdyTMYprGi6YbgO5AEY3ZnfZqzOI2zywm4HbbVaweiG8rQbHA%3D%3D&pid=' + str(
                i) + '&callback=jsonp' + str(i)
            yield scrapy.Request(url=url,callback=self.leibie,meta={'type':leilist[idlist.index(i)]},dont_filter=True)


    def leibie(self,response):
        b = json.loads(response.text[11:-1])
        #print(b)
        count = 1
        types = response.meta['type']


        while count <= 3:
            c = b['data']['topic' + str(count)]['list']
            for i in c:

                zz = re.compile(r'.*?/(.*?)/(\d*)?.*?')
                xiangqing = re.findall(zz,i['link'])
                url = 'http://list.mogujie.com/search?version=8193&ratio=3%3A4&cKey=15&page=1&sort=pop&ad=0&fcid=' + xiangqing[0][1] + '&action=' + xiangqing[0][0]
                yield scrapy.Request(url=url,callback=self.xiangqing,dont_filter=True,meta={'types':types,'fenlei':i['title']})
            count += 1

    def xiangqing(self,response):
        types = response.meta['types']
        fenlei = response.meta['fenlei']
        mnn = json.loads(response.text)
        mnnlist = mnn["result"]["wall"]["docs"]
        xiangqinglist = []
        for gg in mnnlist:
            title = gg['title']
            img = gg['img']
            add = gg['clientUrl']
            xiangqinglist.append({'标题':title,'图片链接':img,'地址':add})

        yield {types:{fenlei:xiangqinglist}}