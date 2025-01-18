import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
browserSortedVeggies = []
# Headless mode - browser opens in invisible mode
chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument('headless')
chromeoptions.add_argument('--ignore-certicate-error')
service_obj1 = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj1,options=chromeoptions)
driver.implicitly_wait(3)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names into list -> veggieList
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggieWebElements:
    browserSortedVeggies.append(element.text)

originalSortedList = browserSortedVeggies.copy()

# sort this list using python methods -> sortedList
browserSortedVeggies.sort()

# veggieList == sortedList
print(originalSortedList)
print(browserSortedVeggies)
assert originalSortedList == browserSortedVeggies
