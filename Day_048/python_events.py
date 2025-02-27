from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

driver.get('https://www.python.org/')

event_container = driver.find_element(By.ID, "content").find_element(By.CLASS_NAME, "event-widget")
event_names = event_container.find_elements(By.TAG_NAME, "li")

events = {}

for i in range(len(event_names)):
    events[i] = {
        "time": event_names[i].find_element(By.TAG_NAME, "time").text,
        "name": event_names[i].find_element(By.TAG_NAME, "a").text
    }

print(events)

driver.quit()