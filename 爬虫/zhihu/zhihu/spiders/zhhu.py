# -*- coding: utf-8 -*-
import scrapy
import json
import re

class ZhhuSpider(scrapy.Spider):
    name = 'zhhu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v3/feed/topstory?action_feed=True&limit=7&session_token=9ef93c8cda190857fac19ba15b6db30c&action=down&after_id='+str(i)+'&desktop=true' for i in range(6,7,7)]

    def parse(self, response):
        jsons = json.loads(response.text)['data']

        for i in jsons:
            laji = i['target'].get('question')
            two = i['target']['id']
            if laji != None:
                one = laji['id']
                urll1 = f"https://www.zhihu.com/question/{str(one)}/answer/{str(two)}"
                urll2 = f"https://www.zhihu.com/api/v4/questions/{one}/related-knowledge-commodities?answer_id=473525905&include=data%5B%3F(type%3Dlive)%5D.speaker%2Cseats%2Creview_score"
                yield scrapy.Request(url=urll1,callback=self.huida,meta={'url':urll2})

    def huida(self,response):
        url = response.meta['url']

        plcount = re.findall('查看全部(.*?)个回答', response.text)[0]
        guanzhu = re.findall('关注者.*?title="(\d+)">', response.text, re.S)[0]
        beiliulan = re.findall('被浏览.*?title="(\d+)">', response.text, re.S)[0]
        types = re.findall('keywords"\scontent="(.*?)"', response.text)[0]

        yield scrapy.Request(url,callback=self.xianqging)


    def xianqging(self,response):
        #quests = json.loads(response.text)['data'][0]['question']['title']
        for i in json.loads(response.text)['data']:
            name = i['author']['name']
            qianming = i['author'].get('headline')
            qianming = ''.join(re.findall('([^a-z/\"<>=])', qianming))

            content = ''.join(re.findall('<p>([^a-z\"]*?)</p>', i['content']))
            zan = i['voteup_count']
            token = i['author']['url_token']
            print(qianming)
            print(content)
            print(zan)
            print(token)
