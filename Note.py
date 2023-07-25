Ubuntu
安裝時看不到下一步! alt+滑 可以移動視窗

安裝無蝦米
sudo apt-get install fcitx-table-boshiamy

解決VirtualBox無法雙向複製貼上
1.裝置→共用剪貼→雙向
2.sudo apt install virtualbox-guest-x11
3.sudo VBoxClient --clipboard

確認一下python的版本
type python python2 python3
設一下別名
alias python='python3'
alias py='python3'

或使用這個
sudo apt install python-is-python3

安裝PIP
1.更新
 sudo apt-get update
 sudo apt-get upgrade
2.sudo apt-get install python-pip 
3.pip -V 
#----------------------------------------------------------------------------------------------------
虛擬環境
安裝 virtualenv (以 Python3 為例)
$ sudo apt-get install python3-pip
$ pip3 install virtualenv

建立虛擬環境
建立前要先知道你想使用的 Python 版本放在哪，假設我想使用 Python3
$ which python3
得到路徑後使用以下指令建立
$ virtualenv -p <python路徑> <想創建的環境名稱>
啟動虛擬環境
建立後可以在目錄發現多了一個環境名稱的資料夾，在終端機中進去 source activate 這個檔案即可啟動虛擬環境
$ source <環境名稱>/bin/activate
成功後會看到終端機名稱前方出現 (<環境名稱>)，如下
(<環境名稱>)$ 
離開虛擬環境
(<環境名稱>)$ deactivate

#----------------------------------------------------------------------------------------------------

# Ubuntu 系統中的selenium設定
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#參數設定
service = Service(executable_path=r'/home/cat/Python/chromedriver')
driver = webdriver.Chrome(service=service)
driver.set_window_size(1280, 800)
