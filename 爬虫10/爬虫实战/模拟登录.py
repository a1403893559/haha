from fake_useragent import UserAgent
from selenium import webdriver
# ua = UserAgent()
# print(ua.chrome)
# print(ua.ie)
# print(ua.random)
import requests
import lxml
import os
import time
drive = webdriver.Chrome(executable_path='/home/run/桌面/chromedriver')

drive.get('https://github.com/login')
#确保网页加载出来
drive.implicitly_wait(10)
drive.find_element_by_id('login_field').send_keys('a1403893559')
drive.find_element_by_id('password').send_keys('a13943469337')
drive.find_element_by_class_name('btn-block').click()
drive.implicitly_wait(10)
drive.find_element_by_class_name('name').click()
drive.find_element_by_xpath('//*[@id="user-links"]/li[3]/details/ul/li[3]/a').click()
print(drive.get_cookies())

# cookie_jj = ''
# for cookie in drive.get_cookies():
#     print(type(cookie))
#     cookie_jj += cookie['name']+'+'+cookie['value']+';'
#
#
# print(cookie_jj[:-2])

url = 'https://github.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',

}
cookes={'Cookie':'__guid=58162108.1331197534790305300.1514447976846.2705; _octo=GH1.1.1944150890.1514447995; _gat=1; _ga=GA1.2.1922992489.1514447995; tz=Asia%2FShanghai; user_session=L58V900M8axLJXPaDfHvhiYePltttB-IB55yHfEcZ9UWW4O8; __Host-user_session_same_site=L58V900M8axLJXPaDfHvhiYePltttB-IB55yHfEcZ9UWW4O8; logged_in=yes; dotcom_user=a1403893559; _gh_sess=T1g4Zm55MWUrS0ZWVExGZCtyK0c0UnNYQ1hLSmRrNm5qWjlUM2cvaDdTN2pPZDd6TjE4Y1FIQWVZYVJnU1RjSU9aV1EyRUNQcDJuOTRqWHlFSGRxc2I0eEtsZEJTQVRQcEhPQ2JPRkdPK3NSSFpuNWNMYlROS3J1MlYxZk1vNVB4c0ZNNm1XTFJOYTFIN1JJUlhWVmJOeHhLU2lGK29mWmJLN1lma2Z3WXZPWDN0cjh0S25wRGY0UVdyNzFrWFg4UjkvLzBBa2NOblkrY1U4dmE2R1lLUzVyNFkxRUhkeHJVYzNIclZjN2ZEUT0tLXRhYUtUT0hWeU5GWTlrU2hEdDhoK0E9PQ%3D%3D--453ab1ae5c3c04638ade878e4c94a53581f8827e'}

drive.get(url)

for cookie in drive.get_cookies():
    # print(type(cookie))
    print(cookie['name'],cookie['value'])

# response = requests.get(url,headers=headers,cookies=cookes)
# a = open('git.txt','w')
# a.write(response.text)
# print(response.text)

