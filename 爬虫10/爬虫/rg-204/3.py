import requests
import json
url = 'https://www.jianshu.com/collections/83/editors?page=1'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
response = requests.get(url,headers=headers)
print(response.text)