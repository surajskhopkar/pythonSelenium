import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expected_list = ['Cucumber - 1 Kg','Raspberry - 1','Strawberry - 1']
service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get(url='https://rahulshettyacademy.com/seleniumPractise')
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys('ber')
time.sleep(3)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

# Chaining
for result in results:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)

totalAmount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert totalAmount == sum

driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
FinalAmount = float(driver.find_element(By.CSS_SELECTOR, "span[class='discountAmt']").text)
assert FinalAmount < float(totalAmount)