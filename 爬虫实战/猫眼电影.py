import os
import requests
from bs4 import BeautifulSoup
import ssl
import pymysql
db = pymysql.connect('localhost','root','139434','爬虫',use_unicode=True,charset='utf8')
kk = db.cursor()


start = int(input('输入你开始的页'))
end = int(input('输入结束的页'))
headers={
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}
cs = end - start
s = 0
cc = (int(start)-1) * 12
while s <= cs:

    url = 'http://maoyan.com/cinemas?offset='+ str(cc)
    dx = requests.get(url,headers=headers)
    context = ssl._create_unverified_context()
    dx = dx.content.decode('utf-8')
    soup = BeautifulSoup(dx)

    a = soup.find_all('a',attrs={'class':'cinema-name'})
    b = soup.find_all('p',attrs={'class':'cinema-address'})
    print (b)
    for i in a:
        sy =  a.index(i)
        c = b[int(sy)]
        mm = i.get_text()
        clj = "http://maoyan.com"+i.get('href')
        mn = c.get_text()
        print(mn,'\n')
        dk =  open('影院.txt','a')
        ll = i.get_text()+'  '+c.get_text()+ '链接地址:'+clj+'\n'
        dk.write(ll)
        er = "insert into 猫眼 values(0,%s,%s,%s)"
        kk.execute(er,(mm,mn,clj))
        db.commit()
    s += 1
    cc += 12
