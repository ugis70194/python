import time
import getpass
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

tweetstr = ""

driver = webdriver.Chrome("c:/Driver/chromedriver.exe")
driver.set_window_size(100,200)
driver.get("https://twitter.com/login")

user = driver.find_element_by_xpath("//input[@class='js-username-field email-input js-initial-focus']")
password = driver.find_element_by_xpath("//input[@class='js-password-field']")
submit = driver.find_element_by_xpath("//button[@type = 'submit']")

print("username:",end="")
user = input()
password = getpass.getpass()

time.sleep(1)
user.send_keys(user)
time.sleep(1)
password.send_keys(password)
time.sleep(1)
submit.click()

time.sleep(3)

while(tweetstr == "") :
    tweetstr = input()
    time.sleep(3)
    if(tweetstr == "quit") : driver.close()
    else :
        tweet = driver.find_element_by_xpath("//div[@name='tweet']").send_keys(tweetstr)
        time.sleep(2)

        tweet_button = driver.find_element_by_xpath("//button[@class='tweet-action EdgeButton EdgeButton--primary js-tweet-btn']")
        tweet_button.click()
        tweetstr = ""