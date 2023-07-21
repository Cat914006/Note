# 網址會修正XD 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from dotenv import load_dotenv
from PIL import Image
import json
import os
import pandas as pd
import requests
import pytesseract
import pyautogui
import datetime
import pyodbc
import sqlalchemy
import urllib
import sys


# 爬爬的版號
dayversion = datetime.datetime.now().strftime('%Y%m%d_%H')
yesterday = (datetime.date.today() +
             datetime.timedelta(-1)).strftime('%Y/%m/%d')

# 基本使用元件載入
load_dotenv()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.set_window_size(1280, 800)

# db連接字串
connection_string = (
    "Driver={SQL Server Native Client 11.0};"
    f"Server={os.getenv('sqlservername')};"
    f"UID={os.getenv('sqlusername')};"
    f"PWD={os.getenv('sqlpssword')};"
    "Database=yd;"
)
quoted = urllib.parse.quote_plus(connection_string)
engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={quoted}')


def login_first():  # 第一個驗證登入頁面
    driver.find_element(By.ID, 'userId').clear()
    driver.find_element(By.ID, 'userPwd').clear()
    driver.find_element(By.ID, 'userId').send_keys(os.getenv('PXNAME'))
    sleep(1)
    driver.save_screenshot('screenshot3.png')
    img = Image.open('screenshot3.png')
    img = img.crop((760, 260, 840, 290))
    img.save('securityImg3.png')
    verifytext = pytesseract.image_to_string(img, lang='eng',
                                             config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    driver.find_element(By.ID, 'userPwd').send_keys(os.getenv('PXPASS'))
    driver.find_element(By.ID, 'securityId').send_keys(verifytext)
    sleep(2)
    print(verifytext)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    chklogin = soup.find(id='loginMsg')
    # print(chklogin)
    if chklogin is None:
        return 'OK'
    else:
        return 'NG'


def login_second():  # 第二次驗證碼
    for go in range(1, 3):
        js = "window.scrollTo(0, document.body.scrollHeight);"
        driver.execute_script(js)
    sleep(1)
    check2 = driver.find_element(
        By.ID, "saleStaDate").get_attribute('value')
    driver.save_screenshot('screenshot4.png')
    img2 = Image.open('screenshot4.png')
    img2 = img2.crop((415, 376, 492, 404))  
    img2.save('securityImg4.png')
    verifytext2 = pytesseract.image_to_string(img2, lang='eng',
                                              config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    try:
        driver.find_element(By.ID, 'securityId').send_keys(verifytext2)
    except:
        print("本次不用圖認證")
    # pyautogui.moveTo(380, 580, duration=1)
    # 再改一次日期
    js2 = 'document.getElementById("saleStaDate").value=' + \
        '\''+f'{yesterday}'+'\''
    driver.execute_script(js2)
    if yesterday == check2:
        driver.find_element(
            By.XPATH, '//*[@id="btn_search"]').click()
    else:
        return
    sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    chklogin2 = soup.find(id='err_securityImg')
    # print(chklogin)
    if chklogin2 is None:
        return 'OK'
    else:
        return 'NG'


def parameter(de):
    sleep(1)
    driver.get(
        'https://aaa.bbb.com')
    js = "window.scrollTo(0, document.body.scrollHeight);"
    driver.execute_script(js)
    radioButtons = driver.find_elements(
        By.ID, 'qryModeQ2')
    radioButtons[0].click()
    driver.find_element(
        By.XPATH, '//*[@id="prodDiv"]/span/span').click()
    sleep(1)
    # 輸入查詢的銷貨日期
    yesterday = (datetime.date.today() +
                 datetime.timedelta(-1)).strftime('%Y/%m/%d')
    js2 = 'document.getElementById("saleStaDate").value=' + \
        '\''+f'{yesterday}'+'\''
    driver.execute_script(js2)
    sleep(1)
    for go in range(1, 3):
        js = "window.scrollTo(0, document.body.scrollHeight);"
        driver.execute_script(js)
    sleep(2)
    pyautogui.typewrite(de)
    pyautogui.press('enter')

   


# 次變數宣一下
false_list = []
max_retry = 0
info = ""
check2 = ""
dfpcode = pd.DataFrame()
dfall = pd.DataFrame()
# 人生總是會失敗!多試幾次就對了!
while max_retry < 3:
    try:
        # 主要程式啟動點：
        if __name__ == '__main__':
            driver.get(
                'https://aaa.bbb.com)
            sleep(1)
            for i in range(1, 3):
                chksuccess = login_first()
                if chksuccess == 'OK':
                    break
                else:
                    chksuccess = login_first()
                if chksuccess == 'OK':
                    break
            sleep(1)
            driver.get(
                'https://aaa.bbb.com')
            js = "window.scrollTo(0, document.body.scrollHeight);"
            driver.execute_script(js)
            # 點選為產品別
            radioButtons = driver.find_elements(
                By.ID, 'qryModeQ2')
            radioButtons[0].click()
            # 抓所有產品的選項
            soup = BeautifulSoup(driver.page_source, "html.parser")
            select = soup.find("select", {"id": "prodList"})
            option_tags = select.find_all('option')
            prodList = [option.get('value') for option in option_tags]
            for de in prodList:
                if de != prodList[0] and de[0] != '9':  # 0不能用從1開始
                    parameter(de)
                    sleep(3)
                    for j in range(1, 5):
                        chksuccess2 = login_second()
                        if chksuccess2 == 'OK':
                            break
                        else:
                            sleep(1)
                            parameter(de)
                            chksuccess2 = login_second()
                        if chksuccess2 == 'OK':
                            break
                    # 這裡進來先判斷一共有幾頁，和抓一些基本資料
                    sleep(0.5)
                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    count = soup.find("font", {"id": "dataTotalCount"})
                    try:
                        count = int(count.text)  # 如果為0筆這裡會轉換失敗，跳出這圈，反正0不抓。
                    except:
                        continue
                    page = math.floor((count-1)/50)
                    panelbody = soup.find("div", {"class": "panel-body"})
                    lablelist = panelbody.find_all("div")
                    dates = (lablelist[4].text).strip()
                    arr = dates.split('：')
                    date = arr[1].strip()
                    print(de, date, count, page)
                    info += f'{de}, {date}, {count}, {page} '+'\n'
                    for go in range(1, 3):
                        js = "window.scrollTo(0, document.body.scrollHeight);"
                        driver.execute_script(js)
                    sleep(1)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    table = soup.find_all('table')
                    dfpcode = pd.read_html(str(table))[3]
                    # 如果項次不只一頁的話dfpcodedfpcode
                    if page > 0:
                        for i in range(0, page):
                            driver.find_element(
                                By.XPATH, '//*[@id="gridQ2"]/div[3]/a[3]').click()
                            sleep(0.9)
                            soup = BeautifulSoup(
                                driver.page_source, 'html.parser')
                            table = soup.find_all('table')
                            df4 = pd.read_html(str(table))[3]
                            dfpcode = pd.concat([dfpcode, df4], axis=0)
                            sleep(0.5)
                    systypelist = []
                    pcodelist = []
                    pdatelist = []
                    sysverlist = []
                    pcodelen = len(dfpcode)
                    for i in range(0, pcodelen):
                        systypelist.append('銷')
                        pcodelist.append(de)
                        pdatelist.append(date)
                        sysverlist.append(dayversion)
                    dfpcode.insert(0, column="systype",
                                   value=systypelist)  # 將門市代碼塞入明細
                    dfpcode.insert(1, column="pcode",
                                   value=pcodelist)  # 將門市代碼塞入明細
                    dfpcode.insert(2, column="pdate", value=pdatelist)  # 將版號塞入
                    dfpcode.insert(3, column="sysver",
                                   value=sysverlist)  # 將版號塞入
                    dfpcode.columns = ['systype', 'pcode',
                                       'pdate', 'sysver', 'seq', 'scode', 'qty']
                    dfall = pd.concat([dfall, dfpcode], axis=0)
            # print(dfall)
            dfall.to_sql('PX_Psi', engine,

                         if_exists='append', index=False)
            # 寫一下log
            driver.close()
            path = 'example.txt'
            with open(path, 'a') as f:
                f.write(f'銷退檔作業成功完成，版號：{dayversion}'+'\n')
                f.write(f'明細：{info}'+'\n')
                f.close()

            print(f'GOGOGO-銷退檔作業成功完成-版號{dayversion}')

        break
    except Exception as err:
        sleep(1)
        print(err)
        path = 'example.txt'
        with open(path, 'a') as f:
            f.write(f'銷退檔作業失敗，次數：{max_retry}{dayversion}')
            f.write(f'銷退檔作業失敗，原因：{err}'+'\n')
            f.close()
    max_retry += 1
    print(f'試錯了{max_retry}次')
    driver.close()
