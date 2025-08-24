from bs4 import BeautifulSoup
import requests, os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

ZILLOW_URL = config["ZILLOW_URL"]
FORM_URL = config["FORM_URL"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

def get_property_data(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    response = requests.get(url=url, headers=header)
    site_data = response.text

    soup = BeautifulSoup(site_data, "html.parser")
    property_cards = soup.find_all(name="div", class_="StyledPropertyCardDataWrapper")

    return [
        (
            card.a.getText().strip().replace(" |", ","),
            int(card.span.getText().strip("$").replace(",", "")[:4]),
            card.a["href"],
        )
        for card in property_cards
    ]



def submit_data(data):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 3)
    driver.get(FORM_URL)

    for prop in data:
        address_input = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
        price_input = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
        link_input = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
        submit_btn = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))

        address_input.send_keys(prop[0])
        price_input.send_keys(prop[1])
        link_input.send_keys(prop[2])
        submit_btn.click()
        new_response_btn = wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
        new_response_btn.click()

    print(f"All property data submitted ({len(data)}).")

property_data = get_property_data(ZILLOW_URL)
submit_data(property_data)