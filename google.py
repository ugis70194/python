import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

f = open("user_data.json",'r')
user_data = json.load(f)
options = Options()
options.binary_location = user_data["chromePATH"]
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options, executable_path=user_data["chromedriverPATH"])

driver.get("https://www.google.co.jp/")
time.sleep(1)

search = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
search.send_keys("kutimoti")
time.sleep(1)
search.send_keys(Keys.ENTER)

for a in driver.find_elements_by_xpath("//h3[@class='LC20lb']") : 
    print(a.text)

driver.close()

