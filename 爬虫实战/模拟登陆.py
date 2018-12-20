from fake_useragent import UserAgent
from selenium import webdriver
# ua = UserAgent()
# print(ua.chrome)
# print(ua.ie)
# print(ua.random)

drive = webdriver.Chrome(executable_path='/home/run/桌面/chromedriver')

drive.get('https://douban.com')
#确保网页加载出来
drive.implicitly_wait(10)
drive.find_element_by_id('form_email').send_keys('18518753265')
drive.find_element_by_id('form_password').send_keys('ljh123456')
drive.find_element_by_class_name('bn-submit').click()
print(drive.get_cookies())

cookie_jj = ''
for cookie in drive.get_cookies():
    print(type(cookie))
    cookie_jj += cookie['name']+'+'+cookie['value']+';'


print(cookie_jj[:-2])