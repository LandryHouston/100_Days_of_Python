from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

PROMISED_DOWN = 500
PROMISED_UP = 50
EMAIL = config['EMAIL']
PASSWORD = config['PASSWORD']
PHONE = config['PHONE']

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

driver.get('https://twitter.com/login')

time.sleep(2)
email = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
email.click()
email.send_keys(EMAIL, Keys.ENTER)
time.sleep(1)
phone = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
phone.send_keys(PHONE, Keys.ENTER)
time.sleep(1)
password = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys(PASSWORD, Keys.ENTER)

