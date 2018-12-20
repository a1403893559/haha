
from selenium import webdriver
from lxml import etree
import re
import pymysql
import requests
from bs4 import BeautifulSoup
import json
import pymongo

client = pymongo.MongoClient('localhost', 27017)
for h in range(0,100,20):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start={0}'.format(str(h))
    response =  requests.get(url)
    kk = json.loads(response.text)
    div = kk['subjects']
    list1 = []
    item = {}
    #print(div)
    for i in div:

        id = i['id']
        list1.append(id)

    for c in list1:
        url = 'https://movie.douban.com/j/subject_abstract?subject_id='+c
        hehe = requests.get(url)
        js = json.loads(hehe.text)
        item['title'] = js['subject']['title']
        item['img'] = js['subject']['url']
        item['content'] = js['subject']['short_comment']['content']
        item['die'] = js['subject']['directors']
        item['active'] = js['subject']['actors']
        item['duration'] = js['subject']['duration']
        item['region'] = js['subject']['region']
        item['types'] = js['subject']['types']
        item['year'] = js['subject']['release_year']
        #print(title,img,content,die,active,duration,region,types,year)

        db = client.douban
        sifeizhai = db.dou
        sifeizhai.insert(dict(item))




















