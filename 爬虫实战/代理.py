import random
import requests
import pymysql
from lxml import etree
headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
        }

class cha():
    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', '139434', '爬虫', use_unicode=True, charset='utf8')
        self.kk = self.db.cursor()
    def suiji(self):
        cx = """select * from ip"""
        self.kk.execute(cx)
        o  =  self.kk.fetchall()
        suiji = random.choice(o)
        proxies = {
            suiji[3].lower(): suiji[3].lower()+'://' + suiji[1] + ':' + suiji[2],
        }

        print(proxies)
    def chaxun(self):
        start = (int(input('输入页码'))-1)*10
        end = start+10

        cx = """select * from ip limit %s,%s"""%(start,end)
        print(cx)
        self.kk.execute(cx)
        jg = self.kk.fetchall()
        print(jg)

    def paqu(self):
        for i in range(1,21):

            url = 'http://www.xicidaili.com/nn/' + str(i)
            yemian = requests.get(url, headers=headers)
            # yemian =  yemian.content.decode('utf-8')
            yemian = etree.HTML(yemian.text)
            ip = yemian.xpath('//table[@id="ip_list"]/tr/td[2]/text()')
            duankou = yemian.xpath('//table[@id="ip_list"]/tr/td[3]/text()')
            http = yemian.xpath('//table[@id="ip_list"]/tr/td[6]/text()')
            print(ip)
            print(duankou)
            print(http)
            for i in ip:
                sy = ip.index(i)

                if http[int(sy)] == 'HTTPS':
                    url = 'https://www.whatismyip.com/'
                    proxies = {
                        'https': 'https://' + i + ':' + duankou[int(sy)],
                    }
                else:
                    url = 'http://www.xicidaili.com/nn'
                    proxies = {
                        'http': 'http://' + i + ':' + duankou[int(sy)],
                    }
                try:
                    ui = requests.get(url, headers=headers, proxies=proxies, timeout=2)
                    if ui.status_code == 200:
                        print('代理好使')
                        er = """insert into ip values(0,"%s","%s","%s")"""%(i, duankou[int(sy)], http[int(sy)])
                        self.kk.execute(er)
                        self.db.commit()
                        print('代理插入成功')
                except:
                    # er = """insert into ip values(0,"%s","%s","%s")"""%(i, duankou[int(sy)], http[int(sy)])
                    # self.kk.execute(er)
                    # self.db.commit()

                    print('代理不可用')



if __name__ == '__main__':
    obj = cha()
    shuru = int(input('请输入您要干嘛,1为爬取存入,2为随机提取,3为查询数据库'))
    if shuru == 1:
        obj.paqu()
    elif shuru == 2:
        obj.suiji()
    else:
        obj.chaxun()




# for i in list1:
#     sy = list1.index(i)
#     dd = list2[int(sy)][0]
#     ads = list3[int(sy)][0]
#     er = """insert into ip values(0,"%s","%s","%s")"""%(i[0],dd,ads)
#     kk.execute(er)
#     db.commit()
#     print ('添加成功')
# cx = """select * from ip"""
# kk.execute(cx)
# o  =  kk.fetchall()
# print(o)
# for k in o:
#     aa = {'http':'http://'+k[1]+':'+k[2]}
#     proxy_list.append(aa)
#
#
#
# proxy = random.choice(proxy_list)
# print (proxy)
# httpproxy_handler = urllib.request.ProxyHandler(proxy)
# opener = urllib.request.build_opener(httpproxy_handler)
# po = {
#     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
# }
# request = urllib.request.Request('http://www.baidu.com/',headers=po)
#
# response = opener.open(request)
# print (response.status_code)
# print(response.read())