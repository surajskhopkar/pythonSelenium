from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--ignore-certificate-errors')
service_obj1 = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj1, options=chrome_options)
driver.get('https://www.rahulshettyacademy.com/angularpractice')
print(driver.title)

