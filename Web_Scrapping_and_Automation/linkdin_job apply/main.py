from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

sr = Service("C:\Devlopment\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=sr, options=op)

USERNAME = "shachitanandk@gmail.com"
PASSWORD = "Sachita1@6202"

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary").click()
time.sleep(1)

user_block = driver.find_element(By.ID, "username")
user_block.send_keys(USERNAME)
pass_block = driver.find_element(By.ID, "password")
pass_block.send_keys(PASSWORD)
sign_btn = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large").click()
time.sleep(1)

job = driver.find_element(By.CSS_SELECTOR, ".scaffold-layout__list-container li").click()
scave_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button").click()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

follow = driver.find_element(By.LINK_TEXT, "Follow")


action = ActionChains(driver)
# if follow.is_displayed():
#     action.click(on_element=follow).perform()