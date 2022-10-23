from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

sr = Service("C:\Devlopment\chromedriver.exe")
op = webdriver.ChromeOptions()
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')

class InternetSpeedTwitterBot:

    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(service=sr, options=op)


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        accept = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept.click()
        time.sleep(2)
        start_test = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_test.click()
        time.sleep(80)
        download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = download.text
        upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = upload.text
        time.sleep(2)



    def tweet_at_provider(self, email, password):

        time.sleep(4)
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(4)
        email_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_box.send_keys(email)
        email_box.send_keys(Keys.ENTER)
        time.sleep(2)
        pass_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass_box.send_keys(password)
        pass_box.send_keys(Keys.ENTER)
        time.sleep(5)
        compose_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        compose_btn.click()
        time.sleep(3)
        tweet_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet_box.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 150down/100up?")
        time.sleep(2)
        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_btn.click()
        print("tweet completed")
        self.driver.quit()

