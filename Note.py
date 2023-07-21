# Ubuntu 系統中的selenium設定
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#參數設定
service = Service(executable_path=r'/home/cat/Python/chromedriver')
driver = webdriver.Chrome(service=service)
driver.set_window_size(1280, 800)
