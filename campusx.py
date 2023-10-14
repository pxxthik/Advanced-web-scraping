from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

s = Service("C:/Users/Acer/Desktop/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=s)

driver.get("http://google.com")

# fetch the input box using xpath
user_input = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
user_input.send_keys("Campusx")
time.sleep(1)
user_input.send_keys(Keys.ENTER)
time.sleep(1)

link = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[2]/div/div/div/div[1]/div/div/span/a/h3')
link.click()
time.sleep(1)

link2 = driver.find_element(by=By.XPATH, value='//*[@id="1668425005116"]/span[2]/a')
link2.click()
