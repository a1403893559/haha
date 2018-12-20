import urllib.request
import ssl
import requests
import urllib.parse as parse
import os

data = {
    'search_text':'喜剧',
    'cat': 1002,
}
headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
data = parse.urlencode(data)
print (data)
url = 'https://movie.douban.com/subject_search?'+data
print (url)
r = requests.get(url,headers=headers)
ss = open('豆瓣post请求.html','w')
ss.write(r.text)
