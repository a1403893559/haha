# -*- coding:UTF-8 -*-
from urllib.request import Request,urlopen
import urllib.parse as parse
import ssl
#构建一个post请求

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Host':'httpbin.org'
}
data = {
    'pagenum':'3',
    'usename':'我爸是李刚',
    'password':'woshiniba',
}
# data = parse.urlencode(data).encode('utf-8')
data = bytes(parse.urlencode(data),encoding='utf-8')
print(data)
url = 'https://httpbin.org/post'
req = Request(url,data=data,headers=headers,method='POST')
context = ssl._create_unverified_context()
response = urlopen(req,context=context)
print(response.read().decode('utf-8'))