import requests
from bs4 import BeautifulSoup
from  concurrent.futures import ThreadPoolExecutor
import os
import time
import json
from lxml import etree
import pymongo

client = pymongo.MongoClient('localhost', 27017)
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }







def open1(iii):

    count = 0
    count1 = count + 1
    url = 'https://www.jianshu.com'+iii.get('href')
    jinru = requests.get(url,headers=headers)

    jiarusoup = BeautifulSoup(jinru.text,'html5lib')
    o = '/home/run/桌面/简书目录/'+iii.get_text().strip()+'/'+ iii.get_text().strip()+ '.txt'


    name = jiarusoup.select('.name a')
    nei1 = ''
    img1 = ''
    data = jiarusoup.find('span',attrs={'class':'publish-time'})
    nei = jiarusoup.select('.show-content div p')
    img = jiarusoup.select('.show-content div img')
    for i in nei:
        nei1 = nei1+'\n'+i.get_text()+'\n'
    for i in img:
        #print(i.get('data-original-src'))
        #hsw = i.get('data-original-src')[-3:]
        hsw1 = i.get('data-original-src')[-8:-4]
        img2 = 'http:'+i.get('data-original-src')
        houzhui = '.jpeg'

        if not os.path.exists('/home/run/桌面/简书目录/'+iii.get_text().strip()):
            os.mkdir("/home/run/桌面/简书目录/"+iii.get_text().strip(), 0o755)
        else:
            print('存在了就不创建了')
        response = requests.get(img2)
        time.sleep(5)
        pic = open("/home/run/桌面/简书目录/"+iii.get_text().strip()+'/' + hsw1 + houzhui, 'wb')
        #print(response.content)
        pic.write(response.content)
        time.sleep(5)



        img1 = img1 +'\n'+ 'http://upload-images.jianshu.io/'+i.get('data-original-src')+'\n'
        zh = '\n'+'名字:'+'\n'+name[0].get_text()+'\n'+'时间:'+'\n'+data.get_text()+'\n'+'内容:'+'\n'+nei1+'\n'+'图片链接:'+'\n'+img1+'\n'
        print(zh)
        laji = open(o, 'w')
        laji.write(zh)


    return name
def jg2(future):
    response = future.result()
    # print(response)


def down(text):
    xierupool = ThreadPoolExecutor(10)
    soup = BeautifulSoup(text,'html5lib')
    if not os.path.exists("/home/run/桌面/简书目录"):
        os.mkdir("/home/run/桌面/简书目录", 0o755)
    else:
        print('存在了就不创建了')
    title = soup.find_all('a',attrs={'class':'title'})
    for i in title:
        hh = xierupool.submit(open1,(i))
        hh.add_done_callback(jg2)

def  jg(future):
    response = future.result()


def main():
    pool = ThreadPoolExecutor(10)
    for i in range(1,3):

        url = 'https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page='+str(i)
        response = requests.get(url,headers=headers)

        handle = pool.submit(down,(response.text))
        handle.add_done_callback(jg)

    for x in range(1,3):
        url = 'https://www.jianshu.com/collections/83/editors?page={0}'.format(str(x))
        response = requests.get(url,headers=headers)
        list1 = json.loads(response.text)['editors']
        print(list1)
        namelist = list(map(lambda x:x['slug'],list1))
        if len(namelist)==10:
            namelist = namelist[1:]
        else:
            pass
        for k in namelist:
            urll = 'https://www.jianshu.com/u/'+k
            ress = requests.get(urll,headers=headers)
            sou = etree.HTML(ress.text)
            item = {}
            print(ress.url)
            item['name'] = sou.xpath('//a[@class="name"]/text()')
            item['guanzhu'] = sou.xpath('//div[@class="info"]/ul/li[1]/div/a/p/text()')
            item['fensi'] = sou.xpath('//div[@class="info"]/ul/li[2]/div/a/p/text()')
            item['wenzhang'] = sou.xpath('//div[@class="info"]/ul/li[3]/div/a/p/text()')
            item['zishu'] = sou.xpath('//div[@class="info"]/ul/li[4]/div/p/text()')
            item['like'] = sou.xpath('//div[@class="info"]/ul/li[5]/div/p/text()')
            print(item)
        #     db = client.jianshu
        #     sifeizhai = db.wenzhang
        #     sifeizhai.insert(dict(item))







if __name__ == '__main__':
    main()