import requests
from  concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import re
import os

def mulu(url):
    if not os.path.exists("/home/run/桌面/小说目录"):
        os.mkdir("/home/run/桌面/小说目录", 0o755)
    else:
        print('存在了就不创建了')

    hqml = requests.get(url)
    hqml.encoding = 'gbk'
    soup = BeautifulSoup(hqml.text, 'html5lib')
    a = soup.select('.dirconone li a')
    title = soup.find('a',attrs={'class':'article_title'})
    title = title.get_text()

    for i in a:
        print(i.get_text())
        nei = requests.get(i.get('href'))
        nei.encoding='gbk'
        ff = BeautifulSoup(nei.text,'html5lib')
        content = ff.find('div',attrs={'id':'content'})
        print(content.get_text())
        pp = ' '+' '+' '+' '+' '+' '+' '+' '+' '+' '+' '+' '+i.get_text()+'\n'+content.get_text()+'\n'
        xieru = open('/home/run/桌面/小说目录/'+title+'.txt','a')
        xieru.write(pp)
        xieru.close()

    return hqml



def je(future):
    response =  future.result()

    print('可以')







def main():
    pagepool = ThreadPoolExecutor(10)
    bookpool =  ThreadPoolExecutor(10)
    url = 'http://www.quanshuwang.com/list/1_1.html'
    response = requests.get(url)


    soup = BeautifulSoup(response.text,'html5lib')
    a = soup.select('.seeWell li')
    for i in a:
        href = i.select('a')[0].get('href')
        
        zz = re.compile(r'http://www.quanshuwang.com/book_(\d*?).html')
        jg = re.findall(zz,href)
        url = 'http://www.quanshuwang.com/book/'+str(jg[0][0:3])+'/'+str(jg[0])


        handle = bookpool.submit(mulu,(url))
        handle.add_done_callback(je)






    # for i in li:
    #     print(i.get_text())











if __name__ == '__main__':
    main()















