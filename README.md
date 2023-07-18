* 爬蟲的筆記  
最近開始玩Python，主要需求是至各大通路抓取需要的資料  
也許是庫存，也許是訂單，~~也許是罰款明細(XD)~~  
簡單的說就是取代"人"的一些日常。  
雖然我還是不太明白，泱泱大廠開個API怎麼了???   
~~好啦!謝謝大老闆貼心為了台灣經濟出一份力多賞一口飯吃，Python真好玩~~  
相較於4GL!真心不騙 ╮（╯＿╰）╭
---
* 常用的工具  
`不是很完整，必竟才摸了一下下，但因為大家都有防爬，主要的幾個工具該玩的該測的應該多多少少有碰碰!`   
  1. BeautifulSoup  
  大名鼎鼎這碗湯就不多說了，應該是所有Python爬蟲班小萌新的第一堂課xD(稱號Get 大嬸級Python萌新)  
  搭配一下requests，抓抓匯率搞搞股價，感覺學會了Python爬蟲界的全世界!!  
  但還要有一說一的要認真表態BeautifulSoup還是真的非常好用的，怎麼說!就是他很基礎卻也很萬能!  
  常常就是一個轉身又華麗出場。  
  遇到什作業，先抄為敬，來這個網頁來抄一抄就對了。[BeautifulSoup小抄](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/ "游標顯示")

  2. Selenium  
     聽說這個大寶貝的出身是自動化測試工具，怎麼有種被我抓來不務正業的感覺?
     總之他在我的內心是爬蟲的光，是希望!(遠目)  
     基本上他可以抓到畫面上8成的元件，且互動成功!(畫面上、畫面上、畫面上) 嗯~重要的事說三次。  
     他需要搭配使用的瀏覽器設定驅動，這只留我常用的Chrome → [Driver](https://chromedriver.chromium.org/downloads)  
     小抄嘛! 因為就我拿來用的這麼「膚淺」基本上就是記得一個語法就結束了!所以就是需要就GOOGLE一下.
     還真沒特別常用的網頁。就隨意留個介紹網址吧。[Selenium介紹](https://www.selenium.dev/)  
    
     ```Python
        //我的膚淺  回頭看來，真的對這個大寶貝太不敬了。
        driver.find_element(By.ID, 'userId').send_keys(os.getenv('PXNAME'))
     ```
     
     
  4. Pytesseract  
     說到這個Pytesseract，先來談談OCR，光學文字辨識，聽起來好像很利害!嗯~他真的滿利害的!  
     先感謝那些大神們(雙手合十)，再來簡單的說→把圖片中的文字轉化成文字檔等。  
     基本上說到網頁，需要登入的網頁，現在除了少數非常率性、大方、甜美、可人 的~~奇怪~~網站。  
     正常多少都有做一些防爬(保護)的機制，較常見的就是會讓你看難分辨到吐血的圖片、或叫你點一個我不是機器人的申明等...  
     搞的很專業的名詞就是Normal Captcha、reCAPTCHA等等..  
     做為一個好像沒那麼正義的一方???好好的觀查對方的城堡找出~~狗洞?~~???  
     是找出對應的入場證明，方法百百種，而Pytesseract就是圖型驗證網頁的起手式。  
     當你看到登入上面那個醜醜的圖，就是起用PIL+Pytesseract這對~~鴛鴦大盜~~最好時機。  
     這個元件我一樣沒有小抄，這裡留一個設定環境的網頁供參考→ [Pytesseract環境設置](https://lufor129.medium.com/pytesseract-%E8%BE%A8%E8%AD%98%E5%9C%96%E7%89%87%E4%B8%AD%E7%9A%84%E6%96%87%E5%AD%97-b1024f678fac "游標顯示")  
     然後留下讓人看不太懂程式碼xD，但真的就是這樣xD   
     ```Python
     //先想辦法把那個吐血的圖產生出來
     img.save('securityImg.png')
     //再來依那個圖的組合給出合理的辨識參數
     verifytext = pytesseract.image_to_string(img, lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
     //把猜?出來的數字扔給守衛
     driver.find_element(By.ID, 'securityId').send_keys(verifytext)
     ```
     
  6. Pyautogui
     
     
  7.  
   
  Pyautogui  
  pandas  
  pandas


* 流程
---
