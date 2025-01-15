import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')

driver = webdriver.Chrome(service=service_obj)
driver.get(url='https://rahulshettyacademy.com/AutomationPractice/')
time.sleep(3)

radio_buttons = driver.find_elements(By.XPATH, "//input[@name='radioButton']")
print(len(radio_buttons))
for radio_button in radio_buttons:
    if radio_button.get_attribute("value") == 'radio2':
        radio_button.click()
        break

assert radio_button.is_selected() == True


time.sleep(5)
driver.close()



