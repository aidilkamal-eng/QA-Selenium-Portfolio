from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://howlongtobeat.com/login")

button_consent = driver.find_element(By.ID, "onetrust-accept-btn-handler")
button_consent.click()

time.sleep(10)

driver.quit()