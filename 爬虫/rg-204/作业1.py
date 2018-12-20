from selenium import webdriver
from lxml import etree
import re
import pymysql
db = pymysql.connect('localhost','root','139434','爬虫',use_unicode=True,charset='utf8')
kk = db.cursor()

browseDriver = webdriver.Chrome(executable_path='/home/run/桌面/chromedriver')

shuru = input('请输入您要搜啥')
browseDriver.get('https://movie.douban.com/subject_search?search_text={0}&cat=1002'.format(shuru))
response =  browseDriver.page_source
#print(response)
soup = etree.HTML(response)




title = soup.xpath('.//div[@class="title"]/a/text()')
title = title[1:]

img = soup.xpath('//div[@class="item-root"]/a/img/@src')
img = img[1:]
fenshu = soup.xpath('//span[@class="rating_nums"]/text()')
typee = soup.xpath('//div[@class="meta abstract"]/text()')
zuozhe = soup.xpath('//div[@class="meta abstract_2"]/text()')

for i in title:
    sy = title.index(i)

    zx = "insert into mao2 values(0,%s,%s,%s,%s,%s)"
    kk.execute(zx,(i,img[int(sy)],fenshu[int(sy)],typee[int(sy)],zuozhe[int(sy)]))
    db.commit()
    print('成功')





# title = title[1:]
# print(len(title))
# print(len(juji))
# print(len(shifou))
# print(len(fenshu))
# print(len(typee))
# print(len(zuozhe))


