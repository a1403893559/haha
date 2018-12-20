import requests
from bs4 import BeautifulSoup
import json
import pymysql
import re
idlist = []
leilist = []
db = pymysql.connect('localhost','root','139434','爬虫',use_unicode=True,charset='utf8')
kk = db.cursor()

def pzfl():
    response = requests.get('http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery211019971151140352905_1532589442489&pids=110119&appPlat=pc&_=1532589442490')

    a = response.text[42:-1]
    print(a)#切割返回的字符串
    a = json.loads(a)          #利用json改变他变成字典
    a = a['data']['110119']['list'] #字典取值，一层一层的取
    for i in a:                 #取出来的字典的值是一个列表
        idlist.append(i["categoryDetailPid"])
        leilist.append(i["categoryName"])
    for i in idlist:
        url = 'http://mce.mogujie.com/jsonp/makeup/3?token=WPNdZevFbj4azNu7OqMLfXcF1RPfTRnjbC65UDdyTMYprGi6YbgO5AEY3ZnfZqzOI2zywm4HbbVaweiG8rQbHA%3D%3D&pid='+str(i)+'&callback=jsonp'+ str(i)
        response = requests.get(url)
        b = response.text[11:-1]
        b = json.loads(b)
        count = 1
        name = 'topic'
        sy = idlist.index(i)
        dn = leilist[int(sy)]
        xqlist = []
        ljlist = []
        print(dn,':')
        while count<=3:
            c = b['data'][name+str(count)]['list']
            for i in c:
                print (i['title'])
                xqlist.append(i['title'])
                print (i['link'])
                ljlist.append(i['link'])
            count += 1

        for hh in xqlist:
            gsy = xqlist.index(hh)
            cclj = ljlist[int(gsy)]
            rr = "insert into 蘑菇街 values(0,%s,%s,%s)"
            kk.execute(rr,(hh,dn,cclj))
            db.commit()
            print ('成功')
    rr = "delete from 蘑菇街 where name=%s"
    kk.execute(rr,('全部品牌'))
    db.commit()

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

print ('1:为爬总条数')
print ('2:为爬详细的')
ll = int(input('请输入您要干啥'))

if ll == 1:
    pzfl()
elif ll == 2:
    fenye()

