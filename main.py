EMAIL = "joaotesta543@gmail.com"
PASSWORD= "cafe2013"
USERNAME = "botmarquim2"
FOLLOW_ACCOUNT =  "cristiano"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# driver_path = Service("C:\webdeveloper/chromedriver.exe")
import time
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/?hl=pt-br")
time.sleep(2)
email_login =driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
email_login.send_keys(EMAIL)
time.sleep(2)
pass_login =driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
pass_login.send_keys(PASSWORD)
pass_login.send_keys(Keys.ENTER)
time.sleep(4)
search_button = driver.find_element(By.XPATH,'//*[@id="mount_0_0_r4"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a')
search_button.click()
time.sleep(2)
search_account =driver.find_element(By.XPATH,'//*[@id="mount_0_0_iB"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
search_account.send_keys(FOLLOW_ACCOUNT)
time.sleep(2)

account_button = driver.find_element(By.XPATH,'//*[@id="mount_0_0_aY"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div/div/div/div[2]/div/div/span[2]/span')
account_button.click()
time.sleep(2)
followers_button = driver.find_element(By.XPATH,'//*[@id="mount_0_0_iB"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
followers_button.click()



