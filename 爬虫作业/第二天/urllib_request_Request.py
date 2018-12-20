from urllib.request import Request,urlopen
import urllib.parse as parse
import ssl
# import urllib.request as request
# request.urlopen()
#urlopen(官方给我们封装的一个简单的发起请求的方法)
# def __init__(self, url, data=None, headers={},
#                  origin_req_host=None, unverifiable=False,
#                  method=None):
#url:这是我们要请求的目标网址
#data：我们需要出入的相关参数，如果要传入的话必须是bytes类型 
#(如果这个字段有值的话那它默认其实是一个post请求)
#headers：请求头（Accept、cookies、User-Agent、Referer、Connection）
#origin_req_host：指域名或者是IP
#method：请求方式（post、get）

#unverifiable：意思是说用户没有足够的权限来访问资源，
#默认是False，表示我们有权限获取，默认是True，表示我们没有权限获取

#构建一个请求对象呢？
url = 'http://www.1905.com/film/?fr=homepc_menu_news'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
}
#构造了一个get方式的请求对象，设置了url、headers、请求方式
req = Request(url,headers=headers,method='GET')
response = urlopen(req)
# print(response.read())

#构造一个但参数get请求
#https://www.baidu.com/s?ie=utf-8&wd=美女
#https://www.baidu.com/s?ie=utf-8&wd=%E7%BE%8E%E5%A5%B3

#构造一个带参数的get请求
data = {
    'wd':'美女',
    'ie':'utf-8',
}
data = parse.urlencode(data)
url = 'https://www.baidu.com/s?'+ data
print(url)
context = ssl._create_unverified_context()
req = Request(url,headers = headers,method='GET')
response = urlopen(req,context=context)
# r = response.read().decode('utf-8')
# print(response.read().decode('utf-8'))

# 构造一个post请求
data = {
    'wd':'美女',
    'ie':'utf-8',
}
data = parse.urlencode(data).encode('utf-8')
context = ssl._create_unverified_context()
req = Request('https://httpbin.org/post',
data=data,headers=headers,method='POST')
response = urlopen(req,context=context)
print(response.read().decode('utf-8'))




# with open('baidu.html','w') as f:
#     f.write(r) 


#




