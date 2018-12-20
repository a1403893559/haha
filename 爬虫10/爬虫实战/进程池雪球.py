import requests
import json
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor
import csv



headers={
    'Referer':'https://xueqiu.com/',
'Cookie':'device_id=45a0bbf4448206785f6acc0ea1e3a565; aliyungf_tc=AQAAAG2SpTZ9SQMA9kh5auurWluwmIkd; xq_a_token=7443762eee8f6a162df9eef231aa080d60705b21; xq_a_token.sig=3dXmfOS3uyMy7b17jgoYQ4gPMMI; xq_r_token=9ca9ab04037f292f4d5b0683b20266c0133bd863; xq_r_token.sig=6hcU3ekqyYuzz6nNFrMGDWyt4aU; _ga=GA1.2.307789696.1528716506; _gid=GA1.2.1025989167.1531386922; u=941531392472376; Hm_lvt_1db88642e346389874251b5a1eded6e3=1528808282,1528848061,1531386922,1531392472; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1531392472',

'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}



def start_k(url):
    response = requests.get(url,headers=headers)
    #print(response.text)
    jsonfile = json.loads(response.text)
    list1 = jsonfile['list']
    for i in list1:
        types = i['column']
        data = json.loads(i['data'])
        title = data['title']
        ids = data['id']
        content = data['description']
        username = data['user']['screen_name']
        reads = data['view_count']

        imgurl = data['user']['profile_image_url']

        print(types)
        print(reads)
        print(imgurl)

        dict = {'id':ids,'title': title, 'content':content,
                'username': username, 'reads':reads,
                'imgurl':imgurl,'address':types,
                }

        with open('雪球.csv', 'a') as f:
            fieldnames = ['id','title', 'content', 'username', 'reads','imgurl','address']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(dict)




def main(shuru):
    urltou = shuru[:83]
    urlhou = shuru[94:]
    response = requests.get(shuru,headers=headers)
    nextid = json.loads(response.text)
    nextid = nextid['next_max_id']
    #print(urltou)
    #print(urlhou)
    start = int(nextid)
    end = int(nextid)-75
    #print(start)
    #print(end)
    pool = ProcessPoolExecutor(10)
    for i in range(start,end,-15):
        urll = urltou+str(i)+'&count=15'+urlhou
        #print(urll)
        response = requests.get(urll,headers=headers)
        #print(response.text)
        p = Process(target=start_k, args=(urll,))
        p.start()
        p.join()
        #handle.add_done_callback(hehe)

    pool.shutdown(False)

if __name__ == '__main__':
    print('1为头条，2为直播，3为泸深，4为房产，5为港股，6为基金，7为美股，8为私募，9为保险')
    shuru = int(input('请输入您想爬啥'))
    urllist = ['https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=-1',
               'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=6',
               'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=105',
               'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=111',
               'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=102',
               'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=104',
               'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=101',
               'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=113',
               'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=110',
               ]




    main(urllist[shuru-1])