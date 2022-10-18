from pprint import pprint
import smtplib
from bs4 import BeautifulSoup
import requests
import lxml

MYEMAIL = "sachita.nand@yahoo.com"

HEADERS = {
    "Accept-Language" : "en-US,en;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

r = requests.get(url="https://www.amazon.in/Redgear-Pro-Gamepad-Support-Supports/dp/B01FJHV47Q/ref=sr_1_3?crid=LMMFIEQ8Q6LR&keywords=pc+gamepad&qid=1661435980&sprefix=pc+ga%2Caps%2C283&sr=8-3", headers=HEADERS)

sp = BeautifulSoup(r.text, "lxml")
price = sp.find(name="span", class_="a-price-whole").getText().strip(".")

if int(price)<=1000:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MYEMAIL, password="ftxldmwlfacozfdf")
        connection.sendmail(from_addr=MYEMAIL, to_addrs="shachitanandk@gmail.com",
                            msg=f"Subject:price alert\n\nyour product price is droped to {price}")