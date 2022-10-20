from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

sr = Service("C:\Devlopment\chromedriver.exe")
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=sr, options=op)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")  # for cookies click
all_prices = driver.find_elements(By.CSS_SELECTOR, "#store div b")  # For store item price
price_id = driver.find_elements(By.CSS_SELECTOR, "#store div")      # For store item id
cookie_upgrade = {}                                                 # stor Item dic with price and id
for i in range(8):
    price = (int(all_prices[i].text.split("-")[1].strip(" ").replace(",", "")))   #geting price text and removing unwanted value
    cookie_upgrade[price] = price_id[i].get_attribute(name="id") # Getting id of items

five_min = time.time() +  30
timeout = time.time() + 5
while True:
    cookie.click()

    if time.time() > timeout:
        afordabel_upgrades = {}   # checking all possible upgrades
        cookies_couny = int(driver.find_element(By.ID, "money").text.replace(",", ""))  # checking total cookies count
        for cost, id in cookie_upgrade.items():
            if cookies_couny > cost:
                afordabel_upgrades[cost] = id
        highest_upgrade = max(afordabel_upgrades)
        upgrade_id = afordabel_upgrades[highest_upgrade]
        driver.find_element(By.ID, upgrade_id).click()   # Buying upgrades
        timeout = time.time() + 5
    if time.time() > five_min:
        print(driver.find_element(By.ID, "cps").text)
        break

# store_item = {}
# for i in range(8):
#
#     store_item[i] = {"price": int(store_p[i].text.split("-")[1].strip(" ").replace(",", "")),
#                      "item_id": store_i[i].get_attribute(name="id")}
# print(store_item)
