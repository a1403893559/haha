import threading
import requests
import json
from lxml import etree
import queue

class ThreadCrawl(threading.Thread):
    def __init__(self,name,pageQueue,dataQueue):
        super(ThreadCrawl, self).__init__()
        self.name = name
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
        }

    def run(self):
        while not self.pageQueue.empty():
            page = self.pageQueue.get()
            furl = 'https://www.qiushibaike.com/8hr/page/'+str(page)+'/'
            response = requests.get(furl,headers=self.headers)
            # print(response.text)
            a = response.text
            if response.status_code == 200:
                self.dataQueue.put(a)
            print('跑起来')

def main():
    pageQueue  = queue.Queue(15)
    dataQueue = queue.Queue()
    for i in range(1,14):
        pageQueue.put(i)

    xcname = ['韩芳','田静','王含青','小胡','小杜']

    for name in xcname:
        thread = ThreadCrawl(name,pageQueue,dataQueue)
        thread.start()
        print (name)

main()
if __name__ == '__main__':
    main()
