import time

from selenium import webdriver

driver = webdriver.Chrome("C:/Selenium/USTSV/0917/WebDriver/chromedriver/chromedriver.exe")

driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_id("tsf").click()
time.sleep(2)
driver.close()
driver.quit()
print("test completed")
