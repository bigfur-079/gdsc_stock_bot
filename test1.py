#爬取股票
#將資料透過telegram bot回報

from email import message
import requests
from bs4 import BeautifulSoup
import time

stock = ["1101", "2330", "5347"] #要爬的股票

for i in range(len(stock)):
    url = "https://tw.stock.yahoo.com/quote/"+stock[i]+".TW"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    #根據tag和class取得股價
    price = soup.find("span", class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)", "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)", "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"])
    
    if price == None:
        url = "https://tw.stock.yahoo.com/quote/"+stock[i]+".TWO"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        price = soup.find("span", class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)", "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)", "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)"])
    
    message = '股票'+stock[i]+'的即時價格為：' + price.getText()
    token = '6770733479:AAFtV9dSkJNpYpS6euKV2YpMmhOouLM64_c'
    chatID = '6475866970'

    #傳送給telegram bot
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatID}&text={message}"
    requests.get(url)

    time.sleep(3)
