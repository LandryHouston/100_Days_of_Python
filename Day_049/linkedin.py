from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
import time

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)

driver.get('https://www.linkedin.com/jobs/')

email = driver.find_element(By.ID, "session_key").send_keys("landryh@landryhouston.com")
password = driver.find_element(By.ID, "session_password").send_keys("Lan.Hou_1999!", Keys.ENTER)
time.sleep(3)

search = driver.find_element(By.XPATH, "//input[@aria-label='Search by title, skill, or company']").send_keys("Data Analyst Remote", Keys.ENTER)
time.sleep(3)
easy_apply = driver.find_element(By.XPATH, '//*[@id="searchFilter_applyWithLinkedin"]').click()
time.sleep(3)


def apply_for_job():
    try:
        driver.find_element(By.CLASS_NAME, "jobs-apply-button").click()
        while True:
            try:
                # Check if "Submit application" button exists, then click it and break
                submit_buttons = driver.find_elements(By.XPATH, '//button[@aria-label="Submit application"]')
                if submit_buttons:
                    submit_buttons[0].click()
                    time.sleep(2)
                    driver.find_element(By.XPATH, '//button[@aria-label="Dismiss"]').click()
                    time.sleep(2)
                    return  # Exit after successful application

                # Click "Continue to next step" or "Review your application"
                next_button = driver.find_element(By.XPATH, '//button[@aria-label="Continue to next step" or @aria-label="Review your application"]')
                next_button.click()
                time.sleep(2)

            except (NoSuchElementException, StaleElementReferenceException):
                break
    except NoSuchElementException:
        return
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, "jobs-apply-button"))


# Iterate through job listings and apply
while True:
    try:
        job_elements = driver.find_elements(By.CSS_SELECTOR, '.scaffold-layout__list li')

        if not job_elements:
            print("No jobs found.")
            break

        for job in job_elements:
            try:
                driver.execute_script("arguments[0].scrollIntoView();", job)  # Scroll to the element
                job.click()
                time.sleep(1)
                apply_for_job()  # Apply for the job
                time.sleep(1)
            except (StaleElementReferenceException, NoSuchElementException):
                continue
            except Exception:
                continue

    except NoSuchElementException:
        break
