import pymssql
from dotenv import load_dotenv
import os
import pandas as pd
from pd_to_mssql import to_sql
import pyodbc
import sqlalchemy
import urllib
import datetime
import re
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import facebook
from dateutil.parser import parse
import json
from geopy.geocoders import Nominatim
from time import sleep

# 基本使用元件載入
load_dotenv()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.set_window_size(1280, 800)


def gettxt(link):
    driver.get(link)
    sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    H = soup.find('h1', {'class': 'bookname'})
    path = r'C:\python\Cat\BB.txt'
    with open(path, 'a', encoding='UTF-8') as f:
        f.write(f'{H.get_text()}' + '\n')
    div = soup.find('div', {'id': 'booktxt'})
    for p in div.find_all('p'):
        path = r'C:\python\Cat\BB.txt'
        with open(path, 'a', encoding='UTF-8') as f:
            f.write(f'{p.get_text()}' + '\n')


driver.get(
    'https://readnovel.tw/list/buduanzuosihouwochenglewanrenmidizun/8/')
sleep(3)
soup = BeautifulSoup(driver.page_source, "html.parser")
div = soup.find('div', {'id': 'content_1'})
for link in div.find_all('a'):
    mylinkh = f'https://readnovel.tw'
    mylinkb = link.get('href')
    mylink = mylinkh+mylinkb
    gettxt(mylink)
