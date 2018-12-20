# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
import json,os
from lxml import etree
import pymongo
clict  = pymongo.MongoClient('localhost',27017)
db = clict.weibo
jh = db.weibo


class WeibozhizhuSpider(scrapy.Spider):
    name = 'weibozhizhu'
    allowed_domains = ['weibo.com']
    start_urls = ['https://weibo.com/5492267390/profile?topnav=1&wvr=6&is_all=1']

    def start_requests(self):

        con = list(jh.find())

        if len(con) >0:



            yield scrapy.Request(self.start_urls[0],callback=self.parse,cookies=con[0])





        else:
            driver = webdriver.Chrome(executable_path='/home/run/桌面/chromedriver')
            driver.get('https://weibo.com/')
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('13159622982')
            driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('13943469337')
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="plc_top"]/div/div/div[3]/div[1]/ul/li[5]/a').click()
            cookies = driver.get_cookies()
            driver.get(self.start_urls[0])

            response = etree.HTML(driver.page_source)
            uname = response.xpath('//*[@class="username"]/text()')
            gexing = response.xpath('//*[@class="pf_intro"]/text()')
            guanzhu = response.xpath('//strong[@class="W_f18"]/text()')
            print(uname)
            print(gexing)
            print(guanzhu)
            cookie_dict = {}
            for cookie in cookies:
                #print(cookie['name'], cookie['value'])
                cookie_dict[cookie['name']] = cookie['value']

            jh.insert(dict(cookie_dict))








    def parse(self, response):
        print(response.status)

