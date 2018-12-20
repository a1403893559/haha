import requests
from bs4 import BeautifulSoup
import os
url = 'http://www.83zw.com/book/9/9030/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
            }
uu = requests.get(url)
uu = uu.content.decode("gbk")

soup = BeautifulSoup(uu,"html5lib")
b = soup.select('dd a')

for i in b:
    print (i.get('href'))
    pj = i.get('href')
    urll = 'http://www.83zw.com/book/9/9030/' + str(pj)
    #
    response = requests.get(urll)
    response = response.content.decode("gbk")
    print (response.text)
    sdd = BeautifulSoup(response,"html5lib")

    x = sdd.find('div',attrs={'id':"chapter_content"})
    print (x)
    jr = open('勇者之师.txt','a')
    ru =  '\n' + x.get_text() + '\n'
    jr.write(ru)
    print ('成功')
