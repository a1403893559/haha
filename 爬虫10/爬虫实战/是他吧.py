import json
import  requests

url = 'http://news.baidu.com/widget?id=LocalNews&ajax=json&t=1531118166323'

response= requests.get(url)

hehe = json.loads(response.text)

hehe = hehe['data']['LocalNews']['data']['rows']['first']
for i in hehe:
    for key,value in i.items():
        print(key+':'+value)