from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

sr = Service("C:\Devlopment\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=sr, options=op)

USERNAME = "nandsachitak@gmail.com"
PASSWORD = "Sachita1@"

driver.get("https://tinder.com/")

time.sleep(2)
cookies = driver.find_element(By.XPATH, '//*[@id="c-1560500889"]/div/div[2]/div/div/div[1]/div[2]/button')
cookies.click()
time.sleep(2)
login = driver.find_element(By.XPATH,
                            '//*[@id="c-1560500889"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(2)
try:
    fb_login = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
    fb_login.click()
except NoSuchElementException:
    more_op = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/button')
    more_op.click()
    time.sleep(2)
    fb_login = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
    fb_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

time.sleep(2)

email_box = driver.find_element(By.XPATH, '//*[@id="email"]')
email_box.send_keys(USERNAME)
pass_box = driver.find_element(By.XPATH, '//*[@id="pass"]')
pass_box.send_keys(PASSWORD)
fp_login_btn = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
fp_login_btn.click()

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(6)
allow_location = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div/div/div[3]/button[1]')
allow_location.click()

time.sleep(2)
not_interested = driver.find_element(By.XPATH, '//*[@id="c1006085331"]/main/div/div/div/div[3]/button[2]')
not_interested.click()

for i in range(0, 30):
    time.sleep(4)
    try:
        dislike_btn = driver.find_element(By.XPATH,
                                          '//*[@id="c-1560500889"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]')
        dislike_btn.click()
        time.sleep(2)
    except NoSuchElementException:
        print("no")
        time.sleep(3)
        continue
    except ElementNotInteractableException:
        time.sleep(4)
        dislike_btn_2 = driver.find_element(By.XPATH, '//*[@id="c-1560500889"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]')
        dislike_btn_2.click()
