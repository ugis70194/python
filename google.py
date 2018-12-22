import time
import getpass
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:/Users/ugis/AppData/Local/Google/Chrome SxS/Application/chrome.exe"
options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options, executable_path="c:/Driver/chromedriver.exe")

driver.get("https://www.google.co.jp/")
time.sleep(1)

search = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
search.send_keys("kutimoti")
time.sleep(1)
search.send_keys(Keys.ENTER)

for a in driver.find_elements_by_xpath("//h3[@class='LC20lb']") : 
    print(a.text)

driver.close()

