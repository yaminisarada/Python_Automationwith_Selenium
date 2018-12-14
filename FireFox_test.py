from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#try:
ff_options = webdriver.FirefoxOptions()
ff_options = Options()
ff_options.add_argument("--headless")
#ff_options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=ff_options, executable_path="C:/Selenium/USTSV/0917/WebDriver/geckodriver-v0.16.1-win64/geckodriver.exe")

driver.get("https://google.com")
print(driver.title)

driver.find_element_by_name("q").send_keys("automation step by step")

driver.find_element_by_name("q").send_keys(Keys.ENTER)
time.sleep(2)
driver.close()
driver.quit()
print("completed")


