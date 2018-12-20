import requests


#拉钩https://www.lagou.com/gongsi/

#目标url
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
data = {
    'first':'false',
    'kd':'php',
    'pn':'2',
}
header = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'23',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'user_trace_token=20180530142358-cb356bf0-2e4f-4080-830f-89d838f590e7; LGUID=20180530142358-0986bef8-63d2-11e8-91d4-5254005c3644; WEBTJ-ID=20180606101303-163d2de6ff417-07b7dabc8e8db3-5d4e211f-2073600-163d2de6ff5861; JSESSIONID=ABAAABAAADEAAFI6FB58988F489F53A651A009077CB4D0F; PRE_UTM=m_cf_cpt_360_pc; PRE_HOST=www.so.com; PRE_SITE=https%3A%2F%2Fwww.so.com%2Fs%3Fie%3Dutf-8%26src%3Dhao_360so_b%26shb%3D1%26hsid%3D731ed3cb9eabf747%26q%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_360_pc; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=search_code; _gat=1; SEARCH_ID=cee803ee956540d8ba387f37cca3d067; _gid=GA1.2.1175878485.1528251183; _ga=GA1.2.1159681594.1513594936; LGSID=20180606101427-570f67ae-692f-11e8-9238-525400f775ce; LGRID=20180606104109-11687d09-6933-11e8-9241-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1527661440,1528251183,1528251269,1528251279; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528252870',
    'Host':'www.lagou.com',
    'Origin':'https://www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_php?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token':'None',
    'X-Requested-With':'XMLHttpRequest',
}
response = requests.post(url,data=data,headers=header)
print(response.status_code)
print(response.text)
data = response.json()
print (data)
