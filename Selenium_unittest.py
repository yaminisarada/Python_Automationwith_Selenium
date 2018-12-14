import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Selenium/USTSV/0917/WebDriver/chromedriver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by Step")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)


    def test_search_2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Yamini")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
