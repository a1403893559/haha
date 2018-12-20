import urllib.request
import urllib
import ssl
import os
from bs4 import BeautifulSoup
import requests
context = ssl._create_unverified_context()

url = 'https://www.ugirls.com/'
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
dx = requests.get(url)
dx = dx.content.decode("utf-8")
soup = BeautifulSoup(dx)
for i in soup.find_all('img'):
    print (i.get('data-original'))

    if i.get('data-original') == None:
        continue
    else:
        a = soup.find_all('img').index(i)
        b = str(a) + '.jpg'
        file = open(b, 'wb')
        bb = requests.get(i.get('data-original'))
        # content：图片转换成二进制，进行保存。
        file.write(bb.content)
