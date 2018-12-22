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
driver.get("https://twitter.com/login")

user = driver.find_element_by_xpath("//input[@class='js-username-field email-input js-initial-focus']")
password = driver.find_element_by_xpath("//input[@class='js-password-field']")
log_in = driver.find_element_by_xpath("//button[@type = 'submit']")

print("username:",end="")
user_name = input()
pasw = getpass.getpass()

time.sleep(1)
user.send_keys(user_name)
time.sleep(1)
password.send_keys(pasw)
time.sleep(1)
log_in.click()

time.sleep(3)
submit = False
tweetstr = ""
while True  :
    for TL_user_name in driver.find_elements_by_xpath("//strong[@class='fullname show-popup-with-id u-textTruncate']") :
        print(TL_user_name)

    input_str = input()
    if(input_str == "quit") : 
        driver.close()
        break
    if(input_str == "send") : submit = True
    elif(input_str == "del") : tweetstr = ""
    else : tweetstr += (input_str + '\n')

    if(submit) : 
        time.sleep(1)
        tweet = driver.find_element_by_xpath("//div[@name='tweet']").send_keys(tweetstr)
        time.sleep(1)
        tweet_button = driver.find_element_by_xpath("//button[@class='tweet-action EdgeButton EdgeButton--primary js-tweet-btn']")
        tweet_button.click()
        submit = False