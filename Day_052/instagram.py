from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


EMAIL = config['EMAIL']
PASSWORD = config['PASSWORD']
SIMILAR_ACCOUNT = config['SIMILAR_ACCOUNT']

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

driver.get("https://www.instagram.com/login")

time.sleep(5)
email = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input').send_keys(EMAIL)
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys(PASSWORD, Keys.ENTER)
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/section/div/button').click()
