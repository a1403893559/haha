# -*- coding: utf-8 -*-
import scrapy
import re
import json
from game.items import GameItem


class GamesSpider(scrapy.Spider):
    name = 'games'
    allowed_domains = ['17173.com']
    #利用列表推导式获取所有链接
    start_urls = ['http://top.17173.com/list-2-0-0-0-0-0-0-0-0-'+'0-'+str(i)+'.html' for i in range(0,37)  if i !=0 ]

    def parse(self, response):
        #print(response.text)
        li = response.css('li.item')           #获取所有li标签
        #print()
        #print(len(li))
        for i in li:
            title = i.css('div.con a::text').extract()[0]  #获取游戏名
            ding = i.css('div.c3::text').extract()[0].replace('\n','').strip()    #获取票数

            jilupian = i.css('div.c5::text').extract()[0].replace('\n','').strip()  #获取纪录片
            paiming = i.css('div.c1 em::text').extract()[0]     #获取排名
            href = i.css('div.con a::attr(href)').extract()  #获取详情链接
            #print(href)

            #请求他，然后把这些传值都传到下一个函数里
            yield scrapy.Request(url=href[0],callback=self.xiangqing,meta={'title':title,'ding':ding,'jilupian':jilupian,'paiming':paiming})

    def xiangqing(self,response):
        qian = ','.join(response.xpath('//div[@class="box-mater-cate"]/a/text()').extract())    #获取标签
        types = response.xpath('//ul[@class="list-mater-info"]/li[1]/a/text()').extract()[0]  #获取游戏类型
        language = response.xpath('//ul[@class="list-mater-info"]/li[2]/span[2]/a/text()').extract()[0] #获取语言
        money = response.xpath('//ul[@class="list-mater-info"]/li[3]/span[2]/text()').extract()[0].replace('\n','').strip() #获取收费模式
        pingtai = response.xpath('//ul[@class="list-mater-info"]/li[4]/a/@title').extract()[0]  #获取游戏平台
        kaifa = response.xpath('//ul[@class="list-mater-info"]/li[5]/a/text()').extract_first('')   #获取开发商
        jianjie = response.xpath('//div[@class="mod-mater-intro"]/p/text()').extract_first('').strip()
        img = response.xpath('//div[@class="pn-c1"]//img[1]/@src').extract_first('')
        yunying = response.xpath('//ul[@class="list-mater-info"]/li[7]/span[2]/a/text()').extract_first('')  #获取运营商
        dicts = {'游戏名称':response.meta['title'],'热度':response.meta['ding'],'测试状态':response.meta['jilupian'],'排名':response.meta['paiming'],
                 '标签':qian,'类型':types,'语言':language,'收费模式':money,'平台':pingtai,'开发商':kaifa,'运营商':yunying,'简介':jianjie,'图片地址':img}
        zz = '.*?game-info-(\d+).html'
        shuzi = re.findall(zz,response.url)      #找出对应的json id
        url = f"http://hao.17173.com/api/getGameScheCount?game_codes={shuzi}"  #字符串拼接,拼接出json的url
        yield scrapy.Request(url=url,callback=self.fuli,meta={'dicts':dicts})  #请求并且传值

    def fuli(self,reponse):
        item = GameItem()
        # print(reponse.text[9:-1])
        dicts = reponse.meta['dicts']
        fuli = list(json.loads(reponse.text[9:-1])['data'].values())[0]  #取出json里福利通知我里的数量
        dicts['福利通知我'] = fuli    #字典赋值
        item['content'] = dicts
        #print(item)
        yield item

