import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')

driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.get(url='https://rahulshettyacademy.com/seleniumPractise')

driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys('ber')
time.sleep(3)
# Implicit wait will not work for find_elements method even when empty string is returned it is still valid


results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

# Chaining
for result in results:
    result.find_element(By.XPATH, "div/button").click()


driver.find_element(By.XPATH, "//img[@alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys('rahulshettyacademy')

driver.find_element(By.XPATH, "//button[text()='Apply']").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)




driver.close()