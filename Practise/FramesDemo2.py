import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
service_obj1 = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj1)
driver.implicitly_wait(15)
driver.get('https://practice-automation.com/iframes/')
time.sleep(15)
driver.switch_to.frame(frame_reference='iframe-1')
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='buttons_pzbO']/a").click()
time.sleep(5)
driver.close()