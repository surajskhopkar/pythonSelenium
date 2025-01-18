import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Headless mode - browser opens in invisible mode
chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument('headless')
chromeoptions.add_argument('--ignore-certicate-error')
service_obj1 = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj1,options=chromeoptions)
driver.implicitly_wait(3)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# Scroll to bottom
driver.execute_script(script='window.scrollBy(0,document.body.scrollHeight)')
# Take screenshots
driver.get_screenshot_as_file(filename='screen.png')
time.sleep(5)
driver.close()
