import urllib.request as request
import urllib.parse as parse
import ssl
import urllib
from bs4 import BeautifulSoup
import os
a = 0
b = 0
context = ssl._create_unverified_context()
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
}
while a <= 100:
    data = {
     'wd': '美女',
     'pn':a,}
    data = parse.urlencode(data)
    # print(data)
    url = 'https://www.baidu.com/s?'+data
    print (url)
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req,context=context)

    aa = response.read().decode('utf-8')
    # print(aa)
    filename = 'baidu{0}.html'.format(b)
    c = open(filename,'w')
    c.write(aa)
    a = a+10
    b = b + 1
    c.close()