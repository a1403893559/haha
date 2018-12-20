import requests
import os
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
shuru = input('请输入您想要查询的东西')

for i in range(0,3):
    url = 'https://www.baidu.com/s?wd={0}&pn={1}'.format(shuru,str(i*10))
    print(url)
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    a = open('/home/run/桌面/百度/'+shuru+str(i)+'.txt','w')

    a.write(response.text)

