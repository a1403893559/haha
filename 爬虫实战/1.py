import urllib.request as request
import ssl
import urllib.parse as parse
context = ssl._create_unverified_context()
# response = request.urlopen('http://fanyi.youdao.com/?keyfrom=fanyi.logo',context=context,timeout=5)

# #print(response.read().decode('utf-8'))
# #返回结果
# print(type(response))
# #打印返回结果类型
# print(response.status)
# #打印 返回状态码
# print(response.getheaders())
# #返回响应头全部参数
# #print(response.getheader('Content-Length'))
# #单独或取其中某一个响应头参数

# #timeout请求时间,超过就报错
# #data参数是可选的,如果没有这个参数,那我们发起的请求参数默认是get
# #如果有这个参数,默认post请求

# #创建一个POST请求
datadict = {
    'key':'value'
}
data = parse.urlencode(datadict).encode('utf-8')
print(data)
response =  request.urlopen('http://httpbin.org/post',data=data,context=context)
print(response.read())
# {
#     "args":{},
#     "data":"",
#     "files":{},
#     "form":{"name":"哈哈"},
#     "headers":{"Accept-Encoding":"identity",
#     "Connection":"close","Content-Length":"9",
#     "Content-Type":"application/x-www-form-urlencoded",
#     "Host":"httpbin.org","User-Agent":"Python-urllib/3.6"},
#     "json":null,
#     "origin":"124.202.206.230",
#     "url":"http://httpbin.org/post"
# }


























