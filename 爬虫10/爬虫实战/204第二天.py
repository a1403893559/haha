import requests
from lxml import etree
import os

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}

for i in range(1,34):
    url = 'https://www.readnovel.com/rank/hotsales?pageNum={0}'.format(str(i))
    response = requests.get(url)
    result = etree.HTML(response.text)
    title = result.xpath('//div[@class="book-mid-info"]/h4/a/text()')
    author = result.xpath('//div[@class="book-mid-info"]/p[@class="author"]/a[1]/text()')
    type = result.xpath('//div[@class="book-mid-info"]/p[@class="author"]/a[2]/text()')
    content = result.xpath('//div[@class="book-mid-info"]/p[@class="intro"]/text()')
    update = result.xpath('//div[@class="book-mid-info"]/p[@class="update"]/a/text()')
    img = result.xpath('//div[@class="book-img-box"]/a/img/@src')

    print(title)
    print(author)
    print(type)
    print(content)
    print(update)
    print(img)

    for x in title:
        sy = int(title.index(x))
        path1 = '/home/run/桌面/204第二天/'+(x.strip())
        if not os.path.exists(path1):  # 判断有没有这个路径,如果有就不创建,没有就创建
            os.mkdir(path1, 0o755)
        else:
            print('存在了就不创建了')
        a = open(path1+'/'+(x.strip())+'.txt','w')
        contents = x+'\n'+'\n'+'作者:'+author[sy]+'\n'+'\n'+'类型:'+type[sy]+'\n'+'\n'+'简介:'+content[sy]+'\n'+'\n'+'最近更新:'+update[sy]

        a.write(contents)
        res = 'http:'+img[sy]
        ff = requests.get(res)
        b = open(path1+'/'+(x.strip())+'0.jpeg','wb+')
        b.write(ff.content)

