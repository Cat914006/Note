
import os
import urllib
import datetime
import re
import time
import requests
# from selenium import webdriver
from bs4 import BeautifulSoup
import json
from time import sleep

# 基本使用元件載入
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)
# driver.set_window_size(1280, 800)



def gettxt(link):
    # driver.get(link)
    url = link
    response = requests.get(url)
    sleep(1)
    soup = BeautifulSoup(response.text, "html.parser")
    # H = soup.find('h1', {'class': 'bookname'})
    # path = r'C:\python\Cat\BB.txt'
    # with open(path, 'a', encoding='UTF-8') as f:
    #     f.write(f'{H.get_text()}' + '\n')
    div = soup.find('div', {'id': 'content'})
    for p in div.find_all('p'):
        path = r'D:\python\Cat\BB.txt'
        with open(path, 'a', encoding='UTF-8') as f:
            f.write(f'{p.get_text()}' + '\n')


url = "https://tw.avsohu.com/index/109579.html"
response = requests.get(url)
# html = BeautifulSoup(response.text, "html.parser")

sleep(3)
soup = BeautifulSoup(response.text, "html.parser")
lis = soup.find_all('li')
for li in lis:
    like=li.find('a')
    mylikeb=like.get('href')
    mylinkh = f'https://tw.avsohu.com'
    mylike=mylinkh+mylikeb
    path = r'D:\python\Cat\BB.txt'
    with open(path, 'a', encoding='UTF-8') as f:
        f.write(f'{li.text}' + '\n')
    gettxt(mylike)
    # print(li.text)
    # print(mylike)
  
