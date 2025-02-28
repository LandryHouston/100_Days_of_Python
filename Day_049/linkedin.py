from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

driver.get('https://www.linkedin.com/jobs/')

email = driver.find_element(By.ID, "session_key").send_keys("landryh@landryhouston.com")
password = driver.find_element(By.ID, "session_password").send_keys("Lan.Hou_1999!", Keys.ENTER)
time.sleep(15)
search = driver.find_element(By.XPATH, '//*[@id="jobs-search-box-keyword-id-ember29"]').send_keys("Data Analyst", Keys.ENTER)
time.sleep(5)
easy_apply = driver.find_element(By.XPATH, '//*[@id="searchFilter_applyWithLinkedin"]').click()