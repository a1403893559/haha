from urllib.request import Request,urlopen
# import urllib.request as request
import urllib.parse as parse
import ssl

#urlopen(官方给我们封装的一个简单的发起请求的方法)
# def __init__(self, url, data=None, headers={},
#                  origin_req_host=None, unverifiable=False,
#                  method=None):
# #url:这是我们要请求的目标网址
#ata: 我们要传入的相关参数，如果要传入的话必须是bytes类型
#headers:请求头，（Accept， cookies，User-Agent，Referer， Connection）
#origin_req_host: 是指域名或者是 IP
#unverifiable：意思是说用户没有足够的权限访问资源，默认是False，表示我们有权限获取
#构造一个请求对象呢？
url = 'http://www.1905.com/film/?fr=homepc_menu_news'
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
# 构造了一个get方法的请求对象，设置了url,headers, 请求方式
req = Request(url,headers=headers,method='GET')
response = urlopen(req)
print(response.read())

#构造一个请求
date = {
    'wd':'美女',
    'ie':'utf-8',
    }
url = 'http://www.baidu.com/s?'
date = parse.urlencode(date).encode('utf-8')
print(date)
context = ssl._create_unverified_context()
req = Request(url,data=date, headers = headers,method='GET')
response = urlopen(req,context=context)
print(response.read().decode('utf-8'))
print('完成了')
