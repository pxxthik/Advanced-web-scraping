from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time

s = Service("C:/Users/Acer/Desktop/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=s)

driver.get("https://www.ajio.com/men-backpacks/c/830201001")

old_height = driver.execute_script("return document.body.scrollHeight")

counter = 1
while True:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(0.5)
    counter += 1

    new_height = driver.execute_script("return document.body.scrollHeight")

    print(counter)
    print("old height: ", old_height)
    print("new height: ", new_height)
    print()

    if new_height == old_height:
        break
    old_height = new_height


html = driver.page_source
with open("ajio.html", "w", encoding='utf-8') as f:
    f.write(html)
