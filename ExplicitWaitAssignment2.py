import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expected_list = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actual_list = []

service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get(url='https://rahulshettyacademy.com/seleniumPractise')
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys('ber')
time.sleep(3)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for result in results:
    actual_list.append(result.find_element(By.XPATH,'h4').text)

print(expected_list)
print(actual_list)

assert actual_list == expected_list
