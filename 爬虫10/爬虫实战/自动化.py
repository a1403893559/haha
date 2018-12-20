import pymysql
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time
import json


db = pymysql.connect('localhost','root','139434','爬虫',use_unicode=True,charset='utf8')
kk = db.cursor()
drive = webdriver.Chrome(executable_path='/home/run/桌面/chromedriver')
drive.get('https://www.taobao.com/')
con = input('输入要搜索的东西')
drive.find_element_by_id('q').send_keys(con)  # 选取id为..的框填入值...
drive.find_element_by_css_selector('#J_TSearchForm > div.search-button > button').click()




def down(sy,title,price,renshu,shop,address):
    item = {}
    item['title']= title1 = str(title[int(sy)].get_text())[19:]
    item['price']= price1 = str(price[int(sy)].get_text())
    item['renshu'] = renshu1 = str(renshu[int(sy)].get_text())
    item['shop'] = shop1 = str(shop[(int(sy)+1)*5-1].get_text())
    item['address'] = address1 = str(address[int(sy)].get_text())
    jsonfile = json.dumps(item)
    print(title1,price1,renshu1,shop1,address1)

    a = open('淘宝.json','a+')
    a.write(jsonfile)
    sql = """insert into taobao values(0,%s,%s,%s,%s,%s)"""
    kk.execute(sql,(title1.strip(),price1.strip(),renshu1.strip(),address1.strip(),shop1.strip()))
    db.commit()




def main():


    for i in range(0,3):
        soup = BeautifulSoup(drive.page_source)
        title = soup.select('.row-2 a')
        price = soup.select('.price strong')
        renshu = soup.find_all('div', attrs={'class': 'deal-cnt'})
        shop = soup.select('.shopname span')
        address = soup.select('.row-3 .location')
        for u in title:
            sy = title.index(u)
            down(sy,title,price,renshu,shop,address)
        drive.find_element_by_css_selector("li.item.next a.J_Ajax.num.icon-tag").click()
        time.sleep(5)




if __name__ == '__main__':
    main()


