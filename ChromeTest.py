from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#one way of getting chromoptions without import statement kis below one
#ch_options = webdriver.ChromeOptions()

#Otherway calling chromeoptions with import statement is below
ch_options = Options()
ch_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=ch_options,executable_path="C:/Selenium/USTSV/0917/WebDriver/chromedriver/chromedriver.exe")

driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation test")
driver.find_element_by_id("tsf").click()
print(driver.title)
driver.close()
driver.quit()
print("completed")