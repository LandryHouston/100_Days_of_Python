from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

driver.get('https://secure-retreat-92358.herokuapp.com/')

driver.find_element(By.NAME, value="fName").send_keys("Landry")
driver.find_element(By.NAME, value="lName").send_keys("Houston")
driver.find_element(By.NAME, value="email").send_keys("landryh@landryhouston.com")
driver.find_element(By.CLASS_NAME, value="btn").send_keys(Keys.ENTER) # (By.CSS_SELECTOR, value="form button").click()