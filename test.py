import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')

time.sleep(5)

driver.quit()