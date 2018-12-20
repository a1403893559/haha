import requests
from bs4 import BeautifulSoup
import re
import pymysql
db = pymysql.connect('localhost','root','139434','爬虫',use_unicode=True,charset='utf8')
kk = db.cursor()
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
url = 'http://top.jobbole.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
response = requests.get(url,headers=headers)
response = response.content.decode("utf-8")

soup =  BeautifulSoup(response,'html5lib')
for i in soup.find_all('h3',attrs={'class':"p-tit"}):
    for d in i.find_all('a', attrs={'target': "_blank"}):
        print (d.text)
        list1.append(d.text)
        print (d.get('href'))
        list2.append(d.get('href'))

for i in soup.find_all('div',attrs={'class':'media-body'}):

    try:


        list3.append(i.find('span').get_text())
    except:
        continue

for i in soup.find_all('p',attrs={'class':'p-meta'}):
    sb = i.find_all('span')

    if len(sb) == 3:
        #有评论有类型list4是类型       list5是评论
           #这是第二个span元素  3个就是有类型的
                #这是第三个span元素  评论量
        list4.append(i.select('span')[1].text)
        list5.append(i.select('span')[2].text)
    elif len(sb) == 2:
        if '<i' in str(i.select('span')[1]):
                  #类型布在，评论在
            list5.append(i.select('span')[1].text)
            list4.append('无')
        else:                       #类型在,评论不在
            list4.append(i.select('span')[1].text)
            list5.append('无')

        print (i.select('span')[1].text)
    elif len(sb) == 1:
        list4.append('无')
        list5.append('无')


list1.remove('点这里 »')
list2.remove('http://group.jobbole.com/22945/')
list3.remove(' Java')
print (list1)
print (list2)
print (list3)
print (list4)
print (list5)
print (len(list1))
print (len(list2))
print (len(list3))
print (len(list4))
print (len(list5))

for i in list1:
    sy =  list1.index(i)
    clj = list2[int(sy)]
    data = list3[int(sy)]
    leixing = list4[int(sy)]
    pl = list5[int(sy)]
    print (i,clj,data,leixing,pl)
    er = "insert into 分页 values(0,%s,%s,%s,%s,%s)"
    kk.execute(er,(i,clj,data,leixing,pl))
    db.commit()

