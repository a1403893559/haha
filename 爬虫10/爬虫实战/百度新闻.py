import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import os
url = ['https://news.baidu.com/widget?id=LocalNews&ajax=json&t=1531048219516','https://news.baidu.com/widget?id=civilnews&t=1531048297542','https://news.baidu.com/widget?id=InternationalNews&t=1531048297558',
       'https://news.baidu.com/widget?id=EnterNews&t=1531048297576','https://news.baidu.com/widget?id=SportNews&t=1531048297592',
       'https://news.baidu.com/widget?id=FinanceNews&t=1531048297611','https://news.baidu.com/widget?id=TechNews&t=1531048297680',
       'https://news.baidu.com/widget?id=MilitaryNews&t=1531048297698','https://news.baidu.com/widget?id=InternetNews&t=1531048297721',
       'https://news.baidu.com/widget?id=DiscoveryNews&t=1531048297750','https://news.baidu.com/widget?id=LadyNews&t=1531048298088',
       'https://news.baidu.com/widget?id=HealthNews&t=1531048298119',]
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

for i in url:
    response = requests.get(i,headers=headers)
    response = response.text
# hotzz = re.compile(r'<a.*?href="(http://news.*?)".*?>(.*?)</a>|<a.*?href="(http://www.xinhuanet.*?)".*?>(.*?)</a>|<a.*?href="(http://opinion.*?)".*?>(.*?)</a>|<a.*?href="(http://xinwen.*?)".*?>(.*?)</a>|<a.*?href="(http://finance.*?)".*?>(.*?)</a>|<a.*?href="(https://3w.huanqiu.*?)".*?>(.*?)</a>|<a.*?href="(https://kandian.*?)".*?>(.*?)</a>')
# hot = re.findall(hotzz,response)
# print(hot)
    lal = etree.HTML(response)
    title = lal.xpath('//h2/span[1]/text()|//h2/a[1]/text()')
    print(title)

    zz = re.compile('<a.*?href="(htt.*?)".*?>(.*?)</a>')
    ahref = re.findall(zz,response)
    print(ahref)
    try:
        path1 = '/home/run/桌面/百度新闻/{0}/'.format(title[0])
        if not os.path.exists(path1):  # 判断有没有这个路径,如果有就不创建,没有就创建
            os.mkdir(path1, 0o755)
        else:
            print('存在了就不创建了')
        for i in ahref:
            print(i)
            path2 = path1+i[1].strip()
            if not os.path.exists(path2):  # 判断有没有这个路径,如果有就不创建,没有就创建
                os.mkdir(path1, 0o755)
            else:
                print('存在了就不创建了')
            res = requests.get(i[0])
            print(res.text)
            a = open(path2+i[1]+'.html','w')
            a.write(res.text)
    except:
        continue





















