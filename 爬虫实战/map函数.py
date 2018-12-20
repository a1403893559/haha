#map函数

# list_1 = [1, 2, 3, 4, 5, 6]
#
#
# def f(x):
#     return x * x
#
#
# a = map(f, list_1)
# print(list(a))



#匿名函数
# f = lambda n,m,b,v,c:n+m+b+v+c
#
# print(f(1,2,3,4,5))

#
# 全局变量
# x = 1
# def hanshu():
#     global x
#     x = 5
#
# hanshu()
# print(x)

#filter()函数
# o = [1,2,3,4,5]
#
# def ter(x):
#     return x%2 == 0
#
# new_list = filter(ter,o)
# print(list(new_list))

#reduce函数
#from functools import reduce
# f = lambda n:n*2
# newlist = map(f,range(0,3))
# print(list(newlist))

# a = reduce(lambda x,y:x*y,[1,2,3,4,5])
# print(a)


#  random.rand方法
# import numpy as np
#
# # data = np.random.rand(list_1)
# # print(data)
# # print(data*10)
# # print(data.dtype)
# # print(data.shape)
#
#
# #装饰器
# # def zsq(haha):
# #     def hah():
# #         a = 1
# #         b = 2
# #
# #         print(a,b)
# #         haha()
# #
# #     return hah
# #
# # @zsq
# # def js():
# #     print('呵呵')
# #
# # js()
#
#
# #有道翻译
# # import requests
# # import time
# # import hashlib
# #
# #
# # def main(key):
# #
# #
# #     m = hashlib.md5()
# #     c = "ebSeFb%=XZ%T[KZ)c(sy!"
# #     f = str(int(time.time()*1000))
# #     u = 'fanyideskweb'
# #     m.update((u+key+f+c).encode('utf-8'))
# #     data = {
# #         'i': key,
# #         'from': 'AUTO',
# #         'to': 'AUTO',
# #         'smartresult': 'dict',
# #         'client': u,
# #         'salt': f,
# #         'sign': m.hexdigest(),
# #         'doctype': 'json',
# #         'version': '2.1',
# #         'keyfrom': 'fanyi.web',
# #         'action': 'FY_BY_REALTIME',
# #         'typoResult': 'false'
# #     }
# #     headers = {
# #         'Origin':'http://fanyi.youdao.com/',
# #         'Referer':'http://fanyi.youdao.com/',
# #         'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 55.0.2883.87Safari / 537.36',
# #     }
# #     url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# #     response = requests.post(url,data=data,headers=headers).json()
# #     print(response['translateResult'][0][0]['tgt'])
# #
# #
# # if __name__ == '__main__':
# #
# #     while True:
# #         key = input('请输入您要翻译').strip()
# #         if key=='quit':
# #             break
# #
# #
# #         main(key)
#
#
# # import numpy
# # a = numpy.arange(0,10)
# # y = numpy.sin(a)
# # print(y)
#
# #打开图片
# # from PIL import Image
# #
# # import numpy
# # import os
# #
# # img = Image.open('/home/run/桌面/有意思/生命诚可贵，恋爱需谨慎/0.jpeg')
# #
# # hehe = numpy.array(img)
# # print(hehe.shape)
#
# #列表生成式
# from collections import Iterable
# a = (x*x for x in range(0,10) if x%2==0)
# print(isinstance(a,Iterable))






#array 方法
# list_1 = [0,105,8,90],[2,2,8,3,8,7]
# X,Y = np.meshgrid(x,y)
# data = np.array(list_1)
# print(list(data))

# a = np.array([1,2,3,4])
# print(a.dtype)

#爬视频
# import requests
#
# for i in range(10720,2716):
#
#     # if i < 10:
#     #     pj =  '00'+str(i)
#     # elif i>=10 and i <100:
#     #     pj = '0'+str(i)
#     # else:
#     pj = str(i)
#     print(pj)
#
#     url = 'https://v.yongjiujiexi.com/20180624/PBmZuFEL/1000kb/hls/JgWux4337{0}.jpeg'.format(pj)
#     response = requests.get(url)
#     a = open('/home/run/桌面/视频/复仇者联盟.mp4','ab+')
#     a.write(response.content)


#filter()函数


#print(list(str(y)+'*'+str(i)+'='+str(y*i) for i in range(1,10) for y in range(1,10) if y<=i))
# print(list([i for i in range(2,102)if not[y for y in range(2,i)if i%y==0]]))
# print(list())

# list2 = filter(lambda x:x%x==0,[i for i in range(2,102)if not[y for y in range(2,i-1)if i%y==0]])
# print(list(list2))

#sorted() 函数
# from operator import itemgetter
# def hanshu(num):
#
#     return num[1]
#
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# a = sorted(L,key= itemgetter(1))
# b = sorted(L,key=lambda t:t[1])
# c = sorted(L,key=hanshu)
# print(c)

#闭包

# def father(*args):
#     list1 = []
#     def son():
#
#         for i in args:
#             list1.append(i)
#
#         return list1
#     return son
#
# ww = father(1,2,3,4,6,7,8,9,25)
# print(ww())

#正则匹配 匿名函数  map函数联合使用
# import requests
# import re
#
# url = 'https://www.readnovel.com/book/7987318804042503#Catalog'
# headers = {
#      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
#  }
# response = requests.get(url,headers = headers)
#
# zz = re.compile(r'<div.*?"volume">.*?免费.*?[<a.*?href="(.*?/chapter/\d+/\d+)".*?>(.*?)</a>]+.*?</div>')
# hh = re.findall(zz,response.text)
# zz2 = re.compile('<a.*?href="(.*?/chapter/\d+/\d+)".*?>(.*?)</a>')
# sy = map(lambda x:re.findall(zz2,x),hh)
# #print(hh)
# a  = list(sy)
# print(a)

#装饰器
# def hanshu2(fuc):
#     def son():
#
#         print('调到了')
#         fuc()
#     return son
#
#
#
# @hanshu2
# def hanshu1():
#     print('次类')
#
# hanshu1()


#偏函数
# a = '0101010'
# b = int(a,base=2)
# print(b)

#类继承
# class  students():
#     def __init__(self,coun,name):
#         self.coun = coun
#         self.name = name
#
#     def print_name(self):
#         print(self.name)
#         print(self.coun)
#
#
# a = students(2,'小张')
# a.print_name()


#爬虫实验
# import requests
# from bs4 import BeautifulSoup
# url = 'http://news.baidu.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text,'html5lib')
# text = soup.find_all('a')
# print(text.stripped_strings)
# texxlist = list(map(lambda x:x.get_text(),text))
# #print(texxlist)

#
# def s():
#     x =  2
#     yield t()
#
#
# def t():
#     print('adsad')


#封装pymongo

# import pymongo
#
#
# class MongoHelper:
#
#         def __init__(self,database,collection,host='localhost',port=27017):
#                 '''
#                 初始化参数
#                 :param host: 主机
#                 :param database: 数据库
#                 :param port: 端口号，默认是27017
#                 '''
#                 self.database = database
#                 self.collection = collection
#
#                 client = pymongo.MongoClient(host=host,port=port)
#                 db = client[self.database]
#                 self.cur = db[self.collection]
#         def insert(self,content):
#             try:
#                 self.cur.insert(content)
#                 print('成功')
#             except Exception as ex:
#                 print(ex)
#                 print('失败')
#
#
#         def find(self,wantcontent):
#             contents = '无'
#             try:
#                 contents = list(self.cur.find(wantcontent))
#                 return contents
#
#             except Exception as ex:
#                 print(ex)
#                 print('执行失败')
#
#         def findall(self):
#             contents = '无'
#             try:
#                 contents = list(self.cur.find())
#                 print(contents)
#                 return contents
#
#
#             except Exception as ex:
#                 print(ex)
#                 print('执行失败')
#
#         def update(self,old,new):
#             try:
#                 self.cur.update(old,new)
#                 print('成功')
#
#             except Exception as ex:
#                 print(ex)
#                 print('执行失败')
#
#         def remove(self,contents):
#             try:
#                 self.cur.remove(contents)
#                 print('成功')
#
#             except Exception as ex:
#                 print(ex)
#                 print('执行失败')

# import re

# c = re.compile('(\w)\w+')
# a = str(['abc','sad','sadwq','tr'])
# print(a)
# d = re.findall(c,a)
# print(d)

# 分词程序，逆向最大匹配法
# 输入   严守一把手机关了
dicts = {}
dicts["字典"] = 1
dicts["严守一"] = 1
dicts["一把手"] = 1
dicts["手机"] = 1
dicts["机关"] = 1
dicts["关了"] = 1
print(dicts)


def Segment(sentence):
    strs = ""
    while len(sentence) > 0:
        for i in range(0, len(sentence)):
            cur = sentence[i:]
            if cur in dicts.keys():
                sentence = sentence[0:i]
                strs = cur + '/' + strs


            else:
                if len(cur) == 1:
                    sentence = sentence[0:i]
                    strs = cur + '/' + strs
        print(strs)


sentence = "严守一把手机关了"
print(Segment(sentence))
