from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

driver.get('https://www.amazon.com/gp/product/B01LZAM6TR/ref=ox_sc_saved_image_10?smid=ATVPDKIKX0DER&th=1')

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
price_as_float = float(f"{price_dollar}.{price_cents}")
print(price_as_float)







#driver.close() # Closes tab
driver.quit() # Closes window