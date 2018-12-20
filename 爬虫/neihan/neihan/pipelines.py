# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo                  #导入pymongo包，来操作数据库
import os
import requests
from scrapy.utils.project import get_project_settings    #导入settings的包
class NeihanPipeline(object):



    def __init__(self,client,collections):
        self.client = client                #实例化参数
        self.collections = collections



    @classmethod
    def from_settings(cls,settings):           #类方法,获取来自setting的参数,,ip地址,数据库名称,集合名称
        host = settings['MONGOHOST']            #获取来自setting的ip地址
        port = settings['MONGOPORT']            #获取来自setting的端口号
        db = settings['MONGODB']                #获取来自setting的数据库名称
        cli = settings['MONGOCLI']              #获取来自setting的集合名称
        client = pymongo.MongoClient(host,port) #连接数据库
        colections = client[db][cli]            #连接集合
        return cls(client,colections)     #cls是返回这个类本身,跟self不一样,self是类的实例化对象



  #36到62是保存到本地

    def process_item(self, item, spider):
        qudiao = str(item['content'][0:10]).strip()  # 保存到本地需要设定文件夹名字为内容前10个
        # 但是我发现获取到的标题有空格,一保存就报错,需要把两端的空格去掉
        pathh = "/home/run/桌面/内涵段子/" + qudiao  # 设定路径
        if not os.path.exists(pathh):  # 判断有没有这个路径,如果有就不创建,没有就创建
            os.mkdir(pathh)
        else:
            print('存在了就不创建了')
        a = open(pathh + '/' + item['content'][0:10] + '.txt', 'a')  # 创建文件名字为内容切片的的文件,
        zz = '作者:' + item['zuozhe'] + '\n' + '\n' + item['content'] + '\n'  # 把内容加到一起,保存到文件里
        a.write(zz)

      # 然后是保存图片


        if item['img'] == '暂无':     #判断有没有图片
            pass                      #如果而没有就跳过,pass

        else:

            pathh2 = pathh + '/' + str(item['content'][0:11]) # 这是拼接路径加文件名字

            a = requests.get('https:'+item['img'])  # 请求这个网页，获取响应

            c = open(pathh2, 'wb')  # 以二进制响应保存到本地
            c.write(a.content)
        a.close()



        self.collections.insert(dict(item))   #保存到mongodb数据库
        return item
