import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.get(url='https://rahulshettyacademy.com/angularpractice/')



# locators supported by selenium: ID, Xpath, CSS Selector, Classname, name, Linktext

driver.find_element(By.NAME,"name").send_keys('Selenium')
driver.find_element(By.NAME,"email").send_keys('TestAutomation@gmail.com')
driver.find_element(By.ID,"exampleInputPassword1").send_keys('1234567')
driver.find_element(By.ID,"exampleCheck1").click()
time.sleep(10)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message



# xpath: //tagname[@attribute='value']

driver.close()


