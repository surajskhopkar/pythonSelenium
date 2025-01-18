import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get(url='https://rahulshettyacademy.com/AutomationPractice/')
time.sleep(3)
driver.maximize_window()
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

time.sleep(5)
driver.close()