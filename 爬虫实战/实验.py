import re
import pymysql
import requests
import json
db = pymysql.connect('localhost','root','139434','爬虫',use_unicode=True,charset='utf8')
kk = db.cursor()

def ksp(c):
    page = int(input('输入要爬第几页'))
    url = 'http://list.mogujie.com/search?version=8193&ratio=3%3A4&cKey=15&page='+str(page)+'&sort=pop&ad=0&fcid='+c[0][1]+'&action='+c[0][0]

    print (url)
    mn = requests.get(url)
    mnn = json.loads(mn.text)
    mnnlist = mnn["result"]["wall"]["docs"]
    for gg in mnnlist:
        title = gg['title']
        img = gg['img']
        add = gg['clientUrl']
        print (title,img,add)
        cha = "insert into 爬下来 values(0,%s,%s,%s)"
        kk.execute(cha,(title,img,add))
        db.commit()
        print ('成功了')






def fenye():
    ry = "select distinct type from 蘑菇街"
    kk.execute(ry)

    b = kk.fetchall()
    print (b)
    for i in b:
        r =  "select name from 蘑菇街 where type=%s"
        kk.execute(r,(i[0]))
        a = kk.fetchall()
        print (i[0],':')
        print (a)
    shuru = input('请输入您想要')

    jk = "select clj from 蘑菇街 where name=%s"
    kk.execute(jk,(shuru))
    ret = kk.fetchone()
    b = re.compile(r'.*?//.*?/.*?/(.*?)/(\d*)?.*?')
    c = re.findall(b,ret[0])
    ksp(c)



fenye()