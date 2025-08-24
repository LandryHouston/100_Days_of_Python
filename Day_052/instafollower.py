from random import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

SIMILAR_ACCOUNT = config['SIMILAR_ACCOUNT']
INSTA_USER = config['EMAIL']
INSTA_PASS = config['PASSWORD']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

MIN_TIME = 1.5
MAX_TIME = 4.5

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=10)
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.cooldown()

    def login(self):
        self.username_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        self.username_input.send_keys(INSTA_USER)

        self.password_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        self.password_input.send_keys(INSTA_PASS)

        self.login_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Log in']")))
        self.login_button.click()
        self.cooldown()

    def find_followers(self):
        # Adding a hard sleep here to let the page full load after logging in
        time.sleep(10)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        self.cooldown()

        self.followers_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()=' followers']")))
        self.followers_button.click()
        self.cooldown()

        # Locate scrollable div and scroll 5 times to load followers
        scrollable_popup = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')))
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            self.cooldown()

    def follow(self):
        # Find all follow buttons and click each; sleep in between actions
        self.follow_buttons = self.driver.find_elements(By.XPATH, '//div[text()="Follow"]')
        self.cooldown()
        for button in self.follow_buttons:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                self.cooldown()
                button.click()
                self.cooldown()
            except Exception as e:
                print("Error clicking Follow button because: ", e)

    def cooldown(self):
        wait = uniform(MIN_TIME, MAX_TIME)
        print(f"[Cooldown] Sleeping for {wait:.2f} seconds...")
        time.sleep(wait)