import requests
from bs4 import BeautifulSoup
from  concurrent.futures import ThreadPoolExecutor
import os
import pymysql
from concurrent.futures import ProcessPoolExecutor
from lxml import etree

headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }





db = pymysql.connect('localhost', 'root', '139434', '爬虫', use_unicode=True, charset='utf8')
kk = db.cursor()

def baocun2(company,comtitle,comxingzhi,comwangzhan,comguimo,comgaddress):
    sql = f"insert into gongsi values(0,'{comtitle}','{comxingzhi}','{comwangzhan}','{comguimo}','{comgaddress}','{company}')"
    kk.execute(sql)
    db.commit()


def baocun(xinzi,address,data,xingzhi,jingyan,xueli,count,leibie,span,title,):
    # if not os.path.exists("/home/run/桌面/智联目录"):
    #     os.mkdir("/home/run/桌面/智联目录", 0o755)
    # else:
    #     print('存在了就不创建了')
    #
    # heh = ''
    # for i in span:
    #     heh = heh + i.get_text()+'\n'
    # dk = open('/home/run/桌面/智联目录/'+title+'.txt','w')
    # zh = '薪资:'+xinzi+'\n'+'地址:'+address+'\n'+'时间:'+data+'\n'+'性质:'+xingzhi+'\n'+'经验:'+jingyan+'\n'+'学历:'+xueli+'\n'+'招聘人数:'+count+'类别:'+leibie+'\n'+'详情:'+heh+'\n'
    # dk.write(zh)

    sql1 = f"insert into zhilian values(0,'{title}','{xinzi}','{address}','{data}','{xingzhi}','{jingyan}','{xueli}','{count}','{leibie}','{span}')"

    kk.execute(sql1)
    db.commit()



def xiangxi(url):


    ll = requests.get(url,headers=headers)                     #请求详情页面
    soup = BeautifulSoup(ll.text,'html5lib')
    title = soup.find('title')                              #获取标题
    company = soup.select('.terminalpage-main .tab-cont-box .tab-inner-cont')[1].get_text()  #公司简介
    span = soup.select('.terminalpage-main .tab-cont-box .tab-inner-cont')[0].get_text()    #获取招聘详情
    xinzi = soup.select('.terminal-ul li')[0].strong.get_text()                 #薪资
    address = soup.select('.terminal-ul li')[1].strong.get_text()              #地址
    data = soup.select('.terminal-ul li')[2].strong.get_text()                  #日期
    xingzhi = soup.select('.terminal-ul li')[3].strong.get_text()               #公司性质
    jingyan = soup.select('.terminal-ul li')[4].strong.get_text()               #经验
    xueli = soup.select('.terminal-ul li')[5].strong.get_text()                 #学历
    count = soup.select('.terminal-ul li')[6].strong.get_text()                 #人数
    leibie = soup.select('.terminal-ul li')[7].strong.get_text()                #类别

    zurl = soup.select_one('.company-name-t a').get('href')                     #公司url
    respo = requests.get(zurl,headers=headers)                                  #公司url相应
    zhtml = BeautifulSoup(respo.text,'html5lib')
    zhtml2 = etree.HTML(respo.text)
    #print(zhtml)

    counts = len(zhtml.select('.comTinyDes tr'))                                #公司人数
    print(counts)
    comtitle = zhtml.select_one('.mainLeft div h1').get_text(strip=True)        #公司名称
    comxingzhi = zhtml2.xpath('//table[@class="comTinyDes"]/tr[1]/td[2]/span/text()')[0]   #公司性质
    comguimo = zhtml2.xpath('//table[@class="comTinyDes"]/tr[2]/td[2]/span/text()')[0]      #公司规模
    if counts == 4:                                                            #判断有没有公司连接
        wangzhan = '暂无'
        comguimo = zhtml2.xpath('//table[@class="comTinyDes"]/tr[3]/td[2]/span/text()')[0]
        comaddress = zhtml2.xpath('//table[@class="comTinyDes"]/tr[4]/td[2]/span/text()')[0]


    elif counts == 5:
        wangzhan = zhtml2.xpath('//table[@class="comTinyDes"]/tr[3]/td[2]/span/a/text()')[0]
        comguimo = zhtml2.xpath('//table[@class="comTinyDes"]/tr[4]/td[2]/span/text()')[0]
        comaddress = zhtml2.xpath('//table[@class="comTinyDes"]/tr[5]/td[2]/span/text()')[0]

    else:
        pass

    baocun(xinzi, address, data, xingzhi, jingyan, xueli,count, leibie, span, title)   #调用函数保存招聘信息

    baocun2(company, comtitle, comxingzhi, wangzhan, comguimo, comaddress)          #保存公司信息







def xiangxi2(future):
    print('')




def zhu(text):
    zpool = ThreadPoolExecutor(5)                        #创建线程池

    soup = BeautifulSoup(text,'html5lib')                #关联页面
    a = soup.select('.newlist tr .zwmc div a')           #寻找链接
    for i in a:
        print(i.get('href'))
        jj = zpool.submit(xiangxi,(i.get('href')))      #给线程池添加任务
        jj.add_done_callback(xiangxi2)                  #设置回调
    zpool.shutdown()                        #让主线程等子线程

def zhu2(future):
    print('')


def main():
    pool =  ProcessPoolExecutor()   #创建一个进程池
    for i in range(1,10):            #循环爬取10页

        url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E6%8A%80%E6%9C%AF&sm=0&sg=d2fe0f1c17064ef3a03fe962d94f5239&p='+str(i) #拼接url
        response = requests.get(url,headers=headers)   #请求头
        jj = pool.submit(zhu,(response.text))          #给进程池添加任务
        jj.add_done_callback(zhu2)                      #添加回调
    pool.shutdown()          #设置让主进程等子进程






if __name__ == '__main__':
    main()