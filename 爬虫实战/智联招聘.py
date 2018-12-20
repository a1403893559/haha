from selenium import webdriver
from bs4 import BeautifulSoup
import json
import os,csv
drive = webdriver.Chrome(executable_path='/home/run/桌面/chromedriver')
drive.get('https://www.zhaopin.com/')
drive.find_element_by_xpath('//*[@id="rightNav_top"]/div/div[1]/div/div[2]/div[2]/a[1]').click()
sr = drive.find_elements_by_xpath(".//*[@id='KeyWord_kw2']")
sr[0].send_keys('技术')
drive.find_element_by_class_name("doSearch").click()

# print(drive.page_source)

f = open('雪球.csv', 'a')
fieldnames = ['职位',]
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()

for i in range(0,3):
    soup = BeautifulSoup(drive.page_source)
    a = soup.select('.zwmc div a')
    for i in a:
        print(i.get_text())
        dit = {
            '职位': i.get_text(),
        }


        writer.writerow(dit)


    sr = drive.find_elements_by_xpath(".//*[@id='goto']")
    sr[0].send_keys()
    drive.find_element_by_class_name("next-page").click()


