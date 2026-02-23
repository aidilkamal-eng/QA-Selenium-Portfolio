from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

def melakukanLogin(Username, Password):
    driver.get("https://howlongtobeat.com/login")

    button_consent = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    button_consent.click()

    username_field = driver.find_element(By.ID, "user_name")
    username_field.send_keys(Username)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(Password)

    captcha_checkbox = driver.find_element(By.ID, "checkbox")
    captcha_checkbox.click()

    time.sleep(2)

    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "no-selection")))

    submit_button = driver.find_element(By.NAME, "Submit")
    submit_button.click()



    time.sleep(10)

    driver.quit()