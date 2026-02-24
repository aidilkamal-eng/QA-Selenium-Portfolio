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


    input("Press Enter to close the browser...")

    driver.quit()