import requests
from lxml import etree
import pymongo
client = pymongo.MongoClient('localhost', 27017)

db = client['dangdang']

biao = db['dangdang']


def zhu(url):
    item = {}
    response = requests.get(url)
    htmls = etree.HTML(response.text)
    item['title'] = htmls.xpath('//h1/@title')
    item['content'] = htmls.xpath('//span[@class="head_title_name"]/@title')
    item['hot'] = htmls.xpath('//span[@class="hot"]/a/text()')
    zuozhes = htmls.xpath('//span[@class="t1"]/a[1]/text()')
    if len(zuozhes) <= 1:
        item['chuban'] = '无'
    else:
        item['chuban'] = zuozhes[1]
    item['chupin']  = htmls.xpath('//span[@class="t1"]/a[2]/text()')
    item['zuozhe'] = zuozhes[0]

    #item['chuban'] = zuozhes[1]
    item['talk'] = zuozhes[2]
    item['date'] = htmls.xpath('//span[@class="t1"][3]/text()')
    item['dangdang_price'] = htmls.xpath('//p[@id="dd-price"]/text()')[1]

    item['dianzishu_price'] = htmls.xpath('//a[@dd_name="电子书价"]/text()')
    biao.insert(item)



def  main():
    url = 'http://book.dangdang.com/'
    response = requests.get(url)

    html = etree.HTML(response.text)
    urllist = html.xpath('//div[@class="col eject_left"]')[7]
    urls = urllist.xpath('./dl/dd/a/@href')


    for i in urls:
        response = requests.get(i)
        erji = etree.HTML(response.text)
        three_url = erji.xpath('//ul[@class="bigimg"]/li/a/@href')
        for urll in three_url:
            zhu(urll)



if __name__ == '__main__':
    main()