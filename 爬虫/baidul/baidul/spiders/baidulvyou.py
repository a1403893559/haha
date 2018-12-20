# -*- coding: utf-8 -*-
import scrapy
import json
from baidul.items import BaidulItem
class BaidulvyouSpider(scrapy.Spider):
    name = 'baidulvyou'


    allowed_domains = ['lvyou.baidu.com']
    start_urls = ['https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn='+str(i) for i in range(15,165,10)]
    print(start_urls)

    def parse(self, response):
        item = BaidulItem()
        #print(response.text)
        jsonfile = json.loads(response.text)['data']['notes_list']
        for i in jsonfile:
            #print(i)
            nid = i['nid']
            print(nid)
            item['title'] =i['title']
            item['content'] = i['content']
            item['user'] = i['user_nickname']
            item['zan'] = i['recommend_count']
            item['eyes'] = i['view_count']
            item['count'] = i['reply_count']
            item['huifu'] = i['last_post']['content']
            item['imgurl'] = 'http:'+i['full_url']
            item['userurl'] = 'https://gss0.baidu.com/7LsWdDW5_xN3otqbppnN2DJv/lvpics/pic/item/'+i['avatar_middle']+'.jpg'

            print(item)
            yield item

        #print(jsonfile)

