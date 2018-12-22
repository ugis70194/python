import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver = None 
In_use = True
tweetstr = ""

def Login() : 
    global driver
    f = open("user_data.json",'r')
    user_data = json.load(f)
    options = Options()
    options.binary_location = user_data["chromePATH"]
    options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options = options, executable_path = user_data["chromedriverPATH"])
    driver.get("https://twitter.com/login")

    user_name = user_data["twname"]
    pasw = user_data["twpass"]
    user = driver.find_element_by_xpath("//input[@class='js-username-field email-input js-initial-focus']")
    password = driver.find_element_by_xpath("//input[@class='js-password-field']")
    log_in = driver.find_element_by_xpath("//button[@type = 'submit']")

    time.sleep(1)
    user.send_keys(user_name)
    time.sleep(1)
    password.send_keys(pasw)
    time.sleep(1)
    log_in.click()
    time.sleep(3)
    print("login!")

def submit(tweetstr) : 
    if tweetstr == "" : return None 
    global driver
    driver.find_element_by_xpath("//div[@name='tweet']").send_keys(tweetstr)
    time.sleep(1)
    driver.find_element_by_xpath("//button[@class='tweet-action EdgeButton EdgeButton--primary js-tweet-btn']").click()

def main() :
    global In_use 
    global driver
    global tweetstr

    input_str = input() + '\n'
    time.sleep(0.5)

    if(input_str == "quit\n") : return None
    if(input_str == "send\n") : 
        submit(tweetstr)
        tweetstr = ""
    if(input_str == "del\n") : 
        tweetstr = ""
        input_str = ""
    
    tweetstr += input_str
    input_str = ""
    return main()   

if __name__ == "__main__" :
    Login()
    main()
    driver.close()
