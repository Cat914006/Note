#算是不務正業的小玩具(老大請同事抓取全台全聯的經緯度?? 小可憐~上千家門市呢!(๑•́ ₃ •̀๑))
#從偉大的google找來教學，99%己完成只是小修一下，謝謝大神。
#功能 用CSV檔整理需要的地址，扔上去自動掃，簡單吐回txt檔。

# 全聯地址經緯度
from selenium import webdriver
from time import sleep
import os
import pandas as pd
import datetime


# 爬爬的版號
dayversion = datetime.datetime.now().strftime('%Y%m%d_%H')

# 基本使用元件載入
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.set_window_size(1280, 800)


def get_coordinate(addr, id):
    try:
        # 查詢
        search = driver.find_element(By.ID, "lat")
        search.clear()
        search.send_keys(addr)  # 輸入地址
        button = driver.find_element(
            By.CSS_SELECTOR, '#geo > div.MuiBox-root.jss3 > button')
        button.click()
        sleep(1)
        text = driver.find_element(
            By.XPATH, '//*[@id="geo"]/div[1]/h2')
        lat, lon = float(text.text.split()[0]), float(
            text.text.split()[2])
        driver.refresh()
        print(id, addr, lat, lon)
        # 寫回
        path = 'C:\python\Addr.txt'
        with open(path, 'a') as f:
            f.write(f'{id},{addr},{lat},{lon}'+'\n')
            f.close()
    except:
        print(addr, '發生錯誤')
        err = '請確認地址是否正常'
        path = 'C:\python\Addr.txt'
        with open(path, 'a') as f:
            f.write(f'{id},{addr},{err}' + '\n')
            f.close()
        pass


# 人生總是會失敗!多試幾次就對了!
max_retry = 0
while max_retry < 1:
    try:
        # 主要程式啟動點：
        if __name__ == '__main__':
            # 先讀地址檔的csv
            df = pd.read_csv('PX.csv',
                             encoding='utf-8', quoting=3)
            df = df.reset_index()
            driver.get(
                'https://share-my-location.com/zh-TW/geocoding')
            sleep(5)
            # 一個一個下去查
            for index, row in df.iterrows():
                get_coordinate(row["地址"], row["代碼"],)
            sleep(10)
            print(f'GOGOGO-完成了')

        break
    except Exception as err:
        sleep(1)
        print(err)
    max_retry += 1
    print(f'試錯了{max_retry}次')
