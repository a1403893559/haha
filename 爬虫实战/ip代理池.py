import requests
from concurrent.futures import ThreadPoolExecutor as aqpool
from lxml import etree
import pymysql
import time
db = pymysql.connect('localhost', 'root', '139434', '爬虫', use_unicode=True, charset='utf8')
kk = db.cursor()
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

def paqu(i,sy,http,duankou):


    print('123')



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
            kk.execute(er)
            db.commit()
            print('代理插入成功')
    except:
        # er = """insert into ip values(0,"%s","%s","%s")"""%(i, duankou[int(sy)], http[int(sy)])
        # self.kk.execute(er)
        # self.db.commit()

        print('代理不可用')



def huidiao(futures):
    a = 1





def main():
    pool = aqpool(10)
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
            jj = pool.submit(paqu,(i,sy,http,duankou))
            jj.add_done_callback(huidiao)




if __name__ == '__main__':
    main()