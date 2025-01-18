import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome driver service
# for every chrome browser version there is specific chrome driver service
# driver = webdriver.Chrome()
# driver.get(url='https://www.facebook.com')
# time.sleep(5)

service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)
driver.get(url='https://www.facebook.com')

time.sleep(5)
