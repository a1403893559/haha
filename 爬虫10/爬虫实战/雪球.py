import requests
import json
import re
from bs4 import BeautifulSoup
import threading
import queue
import os

class pqu(threading.Thread):
    def __init__(self,lname,page,title,data,title2):
        self.lname = lname
        self.page = page
        self.data = data
        self.title = title
        self.title2 = title2
        super(pqu, self).__init__()
        self.headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

    def run(self):

            print (threading.current_thread().name)
            url = 'https://xueqiu.com/today'
            a = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(a.text,'html5lib')
            cc = soup.find_all('router-link')

            for i in cc:
                print (i.get_text())
                self.title.put(i.get_text())
                self.title2.put(i.get_text())
                self.page.put(i.get('data-category'))

            while not self.page.empty():
                xtitle = self.title.get()
                xpage = self.page.get()
                print (xtitle)
                pa = {
                    'since_id': -1,
                    'max_id': -1,
                    'count': 10,
                    'category': xpage
                }
                hd = {
                    'Cookie':'aliyungf_tc=AQAAAATWPxo6TQIAvjt5atTqzpMCWyrj; xq_a_token=019174f18bf425d22c8e965e48243d9fcfbd2cc0; xq_a_token.sig=_pB0kKy3fV9fvtvkOzxduQTrp7E; xq_r_token=2d465aa5d312fbe8d88b4e7de81e1e915de7989a; xq_r_token.sig=lOCElS5ycgbih9P-Ny3cohQ-FSA; u=221528716505657; device_id=45a0bbf4448206785f6acc0ea1e3a565; Hm_lvt_1db88642e346389874251b5a1eded6e3=1528716505; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1528719603; _ga=GA1.2.307789696.1528716506; _gid=GA1.2.901935212.1528716506',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
                }
                urll = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?'
                h = requests.get(urll,headers=hd,params=pa)
                h = json.loads(h.text)

                self.data.put(h)
                print (self.data)
class jx(threading.Thread):
    def __init__(self,parse,title,data):
        self.parse = parse
        self.data = data
        self.title = title
        super(jx, self).__init__()
    def run(self):
        while not self.data.empty():
            print (threading.current_thread().name)
            h  = self.data.get()
            title = self.title.get()
            self.xjx(h,title)


    def xjx(self,h,title):
        print (title)
        print (h,'\n')
        if title == '直播':
            for dx in h['list']:

                data = dx['data']

                data = json.loads(data)
                sj = str(data['id'])+str(data['text'])
                print (data['text'])
                print (data['id'])

                dk = open(title+'.txt','a')
                dk.write(sj)

        else:
            for dx in h['list']:
                data = dx['data']
                print (data)
                data = json.loads(data)
                print (data['title'])
                print (data["description"])
                print (data['id'])
                print (data['user']['screen_name']+'.'+dx['column'])

                sj = str(data['title'])+str(data["description"])+str(data['id'])+str(data['user']['screen_name'])+'.'+str(dx['column'])
                dk = open(title+'.txt', 'a')
                dk.write(sj)


def main():


    dxlist = []
    xdxlist = []
    page = queue.Queue(30)
    title = queue.Queue()
    title2 = queue.Queue()
    data = queue.Queue()
    name = ['run1','run2','run3']
    for lname in name:
        thread = pqu(lname,page,title,data,title2)
        thread.start()
        dxlist.append(thread)
    for thread in dxlist:
        thread.join()

    parsename = ['线程1','线程2','线程3']
    for parse in parsename:
        thread = jx(parse,title2,data)
        thread.start()
        xdxlist.append(thread)










if __name__ == '__main__':
    main()