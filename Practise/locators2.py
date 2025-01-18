import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.get(url='https://rahulshettyacademy.com/client/')
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
time.sleep(2)
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys('demo@gmail.com')
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys('Hello@1234')
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys('Hello@1234')
driver.find_element(By.CLASS_NAME,"btn-custom").click()



time.sleep(4)
driver.close()
