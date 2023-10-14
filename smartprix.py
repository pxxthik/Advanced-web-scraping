import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/Acer/Desktop/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=s)

driver.get("https://www.smartprix.com/mobiles")
time.sleep(1)

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(2)

old_height = driver.execute_script("return document.body.scrollHeight")

counter = 1
while True:

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    counter += 1
    time.sleep(1)

    new_height = driver.execute_script("return document.body.scrollHeight")

    print(counter)
    print("old height: ", old_height)
    print("new height: ", new_height)

    if new_height == old_height:
        break

    old_height = new_height


html = driver.page_source
with open("smartprix.html", "w", encoding='utf-8') as f:
    f.write(html)
