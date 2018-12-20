# -*- coding:utf-8 -*-
#'ascii' codec can't encode characters in position 35-36: ordinal not in range(128)
import urllib.request
from urllib import parse
import ssl

#以豆瓣的电影搜索接口为例，构造get请求
def getajax():
    url = 'https://movie.douban.com/j/search_subjects?'
    # https://movie.douban.com/j/search_subjects?page_limit=20&page_start=40&sort=recommend&tag=%E9%9F%A9%E5%89%A7&type=tv
    # 变动的参数
    data = {
        'page_limit':'20',
        'page_start':'40',
        'sort':'recommend',
        'tag':'韩剧',
        'type':'tv',
    }
    #转换成url编码格式（字符串,这里不是post请求不用转换成字节，直接拼接在地址上）
    data = parse.urlencode(data)
    url = url + data
    print('urlencode转换后:'+data,'\n','完整的get请求地址为:'+url)
    requestContext = ssl._create_unverified_context()  #忽略证书
    # Request对象作为urlopen()方法的参数，发送给服务器并接收响应
    response = urllib.request.urlopen(url,context=requestContext)
    #打印结果可以知道获取的结果为一个json串
    print(response.read(),'\n')
    print(type(response),'\n')
    
   
    
    print(response.url,'\n')
    print(type(dict),'\n')
    print(dict,'\n')
   
 
if __name__ == '__main__':
    getajax()