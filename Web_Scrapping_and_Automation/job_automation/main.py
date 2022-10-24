from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ------------------Links ------------------------------------------------------------------------
GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScCCbA5WgJU3-6DkIEa1G1P-Frmbl2LM5w1VZvAV2DMX1NGuw/viewform?usp=sf_link"

ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
# -------------------------------------------------------------------------------------------------


HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
zillo = requests.get(ZILLOW_LINK, headers=HEADERS)
sp = BeautifulSoup(zillo.text, "html.parser")

# -------------------Getting Property Links --------------------------
property_list = sp.select(selector="ul li article div div  a")
initial_link = []
[initial_link.append(item.get("href")) for item in property_list if item.get("href") not in initial_link]


# --------------Converting Links in proper format ---------------------
link_part_add = "https://www.zillow.com"
links_list = []
for item in initial_link:
    if link_part_add in item:
        links_list.append(item)
    else:
        new = "".join([link_part_add, item])
        links_list.append(new)

# ---------------Creating Address list--------------------------------------------
adresses = sp.select(selector="ul li article div div  a address")
adresses_list = [item.getText() for item in adresses]

# ---------------Creating Price list by deleting unnecessary (letters and symbol) in Price -------------
prices = sp.select(selector='span[data-test="property-card-price"]')
price_list = [item.getText().strip("/mo+ 1 bd") for item in prices]
# ---------------------------------------------------------------------------------

sr = Service("C:\Devlopment\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=sr, options=op)


for i in range(len(links_list)):
    driver.get(GOOGLE_FORM_LINK)
    time.sleep(3)
    ques1_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ques1_input.send_keys(adresses_list[i])
    time.sleep(2)

    ques2_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ques2_input.send_keys(price_list[i])
    time.sleep(2)

    ques3_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ques3_input.send_keys(links_list[i])
    time.sleep(2)

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    time.sleep(3)
    # if links_list[i]!=links_list[-1]:
    #     another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    #     another_response.click()
    #     time.sleep(3)

