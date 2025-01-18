import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
name = "Suraj"
service_obj = Service('/Users/surajkhopkar/Library/CloudStorage/OneDrive-Personal/Software_Testing/Selenium/Drivers/'
                      'chromedriver-mac-arm64/chromedriver')

driver = webdriver.Chrome(service=service_obj)
driver.get(url='https://rahulshettyacademy.com/AutomationPractice/')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input[id='name']").send_keys(name)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

# Switch from driver mode to alert mode

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.accept()
# alert.dismiss()
assert name in alert_text




time.sleep(5)
driver.close()