from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
from cryptography.fernet import Fernet
import sys


a = 5 
secret_key = input("google_auth_key: ")
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0")
driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
url = "https://www.instagram.com/accounts/login/"
url0 = "https://www.instagram.com/direct/inbox/"
message = ""
driver.get(url)

key = Fernet.generate_key()
  
fernet = Fernet(key)

encsecret_key = fernet.encrypt(secret_key.encode())
print("original string: ", secret_key)
print("encrypted string: ", encsecret_key)
sleep(a)
#'trackers231342','trackers28946'
un1 = ["trackers2894001"]
c = random.choice(un1)
print(c)
driver.find_element_by_name("username").send_keys(c)
driver.find_element_by_name("password").send_keys("Kerem2894")
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div").click()
sleep(a)
print("encrypted string: ", encsecret_key)
try:
    driver.find_element_by_css_selector(css_selector="button.sqdOP.yWX7d.y3zKF").click()
except:
    pass
driver.find_element_by_css_selector(css_selector="button.aOOlW.HoLwm").click()
#loggined
sleep(3)
driver.get(url0)
sleep(3)
for i in range(1000):
    for i in range(168):
        driver.get(url0)
        sleep(3)
        
        
        try:
            driver.find_element_by_css_selector(css_selector="div._41V_T.Sapc9.Igw0E.IwRSH.eGOV_._4EzTm").click()
            sleep(10)
            driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)

            driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
            sleep(10)   
        except:
            pass

        sleep(10)

    print(secret_key)
    sleep(50000)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
