import time
import getpass
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

print("Please Input Your E-mail Adress")
print("E-mail Adress:",end = "")
email_adress = input()

print("Please Input Your Password")
password = getpass.getpass()

driver = webdriver.Chrome("c:/Driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.co.jp/")
driver.maximize_window()
login_button = driver.find_element_by_xpath("//a[@id = 'gb_70']")
login_button.click()

input_email_adress = driver.find_element_by_xpath("//input[@type = 'email']")
input_email_adress.send_keys(email_adress)
input_email_adress.send_keys(Keys.ENTER)

time.sleep(1)

input_password = driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
input_password.send_keys(password)
time.sleep(1)
input_password.send_keys(Keys.ENTER)


