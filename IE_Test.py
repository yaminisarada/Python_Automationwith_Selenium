from selenium import webdriver


driver = webdriver.Edge(executable_path="C:/Selenium/USTSV/0917/WebDriver/MicrosoftWebDriver.exe")
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").click()
driver.close()
driver.quit()
print("completed")