import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
service_obj1 = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj1)
driver.implicitly_wait(15)
driver.get('https://the-internet.herokuapp.com/iframe')
time.sleep(15)
wait = WebDriverWait(driver, 15)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='page-footer']/div")))
driver.switch_to.frame(frame_reference='mce_0_ifr')
time.sleep(3)
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Let's automate frames")


time.sleep(5)
driver.close()
