import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.get(url='https://rahulshettyacademy.com/AutomationPractice/')
time.sleep(3)
elements = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(elements))
for element in elements:
    if element.get_attribute("value") == 'option2':
        element.click()
        break

assert element.is_selected() == True



time.sleep(5)
driver.close()