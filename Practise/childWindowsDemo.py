import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/geckodriver')
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(3)
driver.get('https://the-internet.herokuapp.com/windows')
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='example']/h3")))

driver.find_element(By.LINK_TEXT, "Click Here").click()
windows_opened = driver.window_handles
print(windows_opened)
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windows_opened[0])
print(driver.find_element(By.TAG_NAME, "h3").text)




time.sleep(5)
driver.close()
