import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')

driver = webdriver.Chrome(service=service_obj)
driver.get(url='https://rahulshettyacademy.com/seleniumPractise')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys('ber')
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

# Chaining
for result in results:
    result.find_element(By.XPATH, "div/button").click()
    time.sleep(1)

driver.find_element(By.XPATH, "//div[@class='cart-preview']").click()


time.sleep(5)
driver.close()