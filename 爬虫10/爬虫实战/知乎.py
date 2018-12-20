import requests
import re
import pymysql
from lxml import etree
db = pymysql.connect('localhost', 'root', '139434', '爬虫', use_unicode=True, charset='utf8')
kk = db.cursor()


headers = {
'cookie':'q_c1=b8bdaa76c78546a3a9ed43ff239d4d62|1508574969000|1508574969000; _zap=a9af7f91-e82c-4564-956c-f26b4e54a41a; d_c0="AHDCw4DitQyPTqcKt-asbZm10P1bIaMs4fY=|1511144510"; __DAYU_PP=ru2vRenfbzzqqAUN3Qf324f451c7140c; z_c0="2|1:0|10:1527639470|4:z_c0|92:Mi4xTDV5V0JnQUFBQUFBY01MRGdPSzFEQ1lBQUFCZ0FsVk5yanY3V3dEVVR2TzRCbWMzTUwzOS1tWUMySzBsY1pRd0dR|6c10649efbd75d45e425fc325d79f539bae5fa4bd7b73ffe764f43bcb97086e2"; _xsrf=gAZfvzgnPtgKfqdoM7tM6WgLLNGCQFDg; q_c1=b8bdaa76c78546a3a9ed43ff239d4d62|1534994066000|1508574969000; __utma=155987696.1238772866.1530665280.1530665280.1535015345.2; __utmz=155987696.1530665280.1.1.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/34577193; tgw_l7_route=ec452307db92a7f0fdb158e41da8e5d8',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}

def userjson(token):
    url = f"https://api.zhihu.com/people/{token}"
    response = requests.get(url,headers=headers)
    s = response.json()
    jzd = s.get('locations', 'my')  # 居住第
    if jzd == 'my':
        jzd = '没有'
    else:
        jzd = s['locations'][0]['name']
    hy = s.get('busines', '匿名用户')  # 所在行业
    if hy == '匿名用户':
        hy = '匿名用户'
    else:
        hy = s['busines'][0]['name']
    gr = s.get('description', '匿名用户')  # 个人简介
    if gr == '':
        gr = '没有'
    return jzd,hy,gr






def user(token):
    url = f'https://www.zhihu.com/people/{token}/activities'
    respon = requests.get(url,headers=headers)
    response = etree.HTML(respon.text)
    name = response.xpath('//span[@class="ProfileHeader-name"]/text()')
    qianming = response.xpath('//span[@class="RichText ztext ProfileHeader-headline"]/text()')
    if name ==[]:
        name =['匿名用户']
    if qianming==[]:
        qianming=['无']
    print(token)
    huida = response.xpath('//span[@class="Tabs-meta"]/text()')
    if len(huida) == 0:
        pass
    else:
        tiwen = response.xpath('//span[@class="Tabs-meta"]/text()')[1]
        wenzhang = response.xpath('//span[@class="Tabs-meta"]/text()')[2]
        zhuanlan = response.xpath('//span[@class="Tabs-meta"]/text()')[3]
        xiangfa = response.xpath('//span[@class="Tabs-meta"][5]/text()')
        zantong = re.findall('获得.*?>(.*?)<.*?赞同',respon.text,re.S)[0]
        bianji = re.findall('参与.*?>(.*?)<.*?编辑',respon.text,re.S)
        shoucang = ','.join(re.findall('ItemValue">(获得.*?谢.*?收藏)<',respon.text,re.S)).replace('\n','').replace(' ','')[0]
        guanzhu = response.xpath('//strong[@class="NumberBoard-itemValue"]/text()')[0]
        usejson = userjson(token)
        print(usejson)
        sql = f"""insert into userdetail values(0,"{name[0]}","{qianming[0]}","{huida[0]}","{tiwen}","{wenzhang}","{zhuanlan}","{xiangfa}",
        "{zantong}","{bianji}","{shoucang}","{guanzhu}","{usejson[0]}","{usejson[1]}","{usejson[2]}")"""
        print('user',sql)
        kk.execute(sql)
        db.commit()
        print('用户插入成功')


def xiangqing(url,pinglun):
    response = requests.get(url,headers =headers)


    quests = response.json()['data'][0]['question']['title']
    for i in response.json()['data']:
        name = i['author']['name']
        qianming = i['author'].get('headline')
        qianming = ''.join(re.findall('([^a-z/\"<>=])',qianming))
        print(qianming)
        content = ''.join(re.findall('<p>([^a-z\"]*?)</p>',i['content']))
        zan = i['voteup_count']
        token = i['author']['url_token']
        sql = f"""insert into wenti values(0,"{name}","{token}","{quests}","{content}","{zan}","{qianming}","{pinglun[0]}","{pinglun[1]}","{pinglun[2]}","{pinglun[3]}")"""
        with open('git.txt','w') as f:
            f.write(sql)
        kk.execute(sql)
        db.commit()
        print('成功')
        user(token)




def all(url):
    response = requests.get(url, headers=headers)
    plcount = re.findall('查看全部(.*?)个回答',response.text)[0]
    guanzhu = re.findall('关注者.*?title="(\d+)">',response.text,re.S)[0]
    beiliulan = re.findall('被浏览.*?title="(\d+)">', response.text, re.S)[0]
    types = re.findall('keywords"\scontent="(.*?)"',response.text)[0]

    return plcount,guanzhu,beiliulan,types

def zhu():
    for i in range(6,21,7):

        url = 'https://www.zhihu.com/api/v3/feed/topstory?action_feed=True&limit=7&session_token=9ef93c8cda190857fac19ba15b6db30c&action=down&after_id='+str(i)+'&desktop=true'
        response = requests.get(url,headers=headers)

        for i  in response.json()['data']:
            two = i['target']['id']
            laji = i['target'].get('question')
            if laji == None:
                continue
            one = laji['id']
            urll1 = f"https://www.zhihu.com/question/{str(one)}/answer/{str(two)}"
            pinglun = all(urll1)


            urll = f"https://www.zhihu.com/api/v4/questions/{one}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=&limit=3&sort_by=default"
            xiangqing(urll,pinglun)

if __name__ == '__main__':
    zhu()