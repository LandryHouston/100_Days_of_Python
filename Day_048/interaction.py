from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

count_articles = driver.find_elements(By.XPATH, '//a[@title="Special:Statistics"]')
print(count_articles[1].text)

count_articles[1].click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)


#driver.quit()