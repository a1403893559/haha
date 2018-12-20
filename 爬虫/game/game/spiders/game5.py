# -*- coding: utf-8 -*-
import scrapy
from game.items import GameItem
import json
class Game5Spider(scrapy.Spider):
    name = 'game5'
    allowed_domains = ['17173.com']
    start_urls = ['http://newgame.17173.com/shouyou/ceshi']

    def parse(self, response):
        #ul1 = response.xpath('//ul[@class="nowlist"]/li')

        title = response.xpath('//ul[@class="nowlist"]/li//h6[@class="tit"]/a/text()').extract()
        href = response.xpath('//ul[@class="nowlist"]/li//h6[@class="tit"]/a/@href').extract()
        ceshi = response.xpath('//ul[@class="nowlist"]/li//p[@class="c3"]/text()').extract()
        types = response.xpath('//ul[@class="nowlist"]/li//i[@class="c4"]/text()').extract()
        address = response.xpath('//ul[@class="nowlist"]/li//span[@class="c7"]/text()').extract()
        title2 = response.xpath('//h6[@class="c1"]/a/text()').extract() + title
        ceshi2 = response.xpath('//p[@class="c3"]/text()').extract() + ceshi
        types2 = response.xpath('//i[@class="c4"]/text()').extract() + types
        href2 = response.xpath('//h6[@class="c1"]/a/@href').extract() + href
        address2 = response.xpath('//span[@class="c7"]/text()').extract() + address


        for i in href2:
            indexs  = int(href2.index(i))
            dicts = {'游戏名称':title2[indexs],'测试状态':ceshi2[indexs],'公司名称':address2[indexs],'类型':types2[indexs]}
            yield scrapy.Request(url=i,callback=self.hehe,meta={'dicts':dicts})
        for u in range(2,10):
            url = 'http://newgame.17173.com/shouyou/ceshi/GetTestListApi?pageSize=30&page='+str(u)
            yield scrapy.Request(url=url,callback=self.jsons)

    def hehe(self,response):
        dicts = response.meta['dicts']
        item = GameItem()
        dicts['标签'] = ','.join(response.xpath('//div[@class="box-mater-cate"]/a/text()').extract())  # 获取标签
        dicts['类型'] = response.xpath('//ul[@class="list-mater-info"]/li[1]/a/text()').extract()[0]  # 获取游戏类型
        dicts['语言'] = response.xpath('//ul[@class="list-mater-info"]/li[2]/span[2]/a/text()').extract_first('') # 获取语言
        dicts['收费类型'] = response.xpath('//ul[@class="list-mater-info"]/li[3]/span[2]/text()').extract()[0].replace('\n',
                                                                                                           '').strip()  # 获取收费模式
        dicts['平台'] = response.xpath('//ul[@class="list-mater-info"]/li[4]/a/@title').extract()[0]  # 获取游戏平台
        dicts['开发商'] = response.xpath('//ul[@class="list-mater-info"]/li[5]/a/text()').extract_first('')  # 获取开发商
        dicts['简介'] = response.xpath('//div[@class="mod-mater-intro"]/p/text()').extract_first('').strip()
        dicts['图片链接'] = response.xpath('//div[@class="pn-c1"]//img[1]/@src').extract_first('')
        dicts['运营商'] = response.xpath('//ul[@class="list-mater-info"]/li[7]/span[2]/a/text()').extract_first('')
        item['content'] = dicts
        yield item

    def jsons(self,response):
        jsonfile = json.loads(response.text)['data']['dataSet']
        print(jsonfile)
        for i in jsonfile:
            title = i['info_chname']
            address = i['company_name']
            href = i['down_url']
            ceshi = i['test_status_name']
            types = i['game_type_name']
            dicts = {'游戏名称':title,'公司名称':address,'测试状态':ceshi,'类型':types}
            yield scrapy.Request(url=href,callback=self.hehe,meta={'dicts':dicts})

        #title = jsonfile['']