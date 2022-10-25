from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

sr = Service("C:\Devlopment\chromedriver.exe")
op = webdriver.ChromeOptions()

USER = "nandsachitak@gmail.com"
PASSWORD = "Sachita1@"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=sr, options=op)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)
        email_box = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_box.send_keys(USER)
        pass_box = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_box.send_keys(PASSWORD)
        pass_box.send_keys(Keys.ENTER)
        time.sleep(3)
        not_save_info = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_save_info.click()
        time.sleep(5)
        notification = self.driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        notification.click()

    def find_followers(self):
        time.sleep(3)
        account = self.driver.get(f"https://www.instagram.com/chefsteps")
        time.sleep(5)
        followers_find = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers_find.click()
        time.sleep(3)
        scroll_window = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_window)
            time.sleep(2)

    def follow(self):
        followers = self.driver.find_elements(By.CSS_SELECTOR, "._aano div button")
        time.sleep(5)

        for item in followers:
            time.sleep(2)
            try:
                item.click()
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                cancel.click()
            except NoSuchElementException:
                limit = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]')
                limit.click()
                print("limit exceeded")


instabot = InstaFollower()
instabot.login()
instabot.find_followers()
instabot.follow()
