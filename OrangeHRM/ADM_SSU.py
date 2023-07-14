import unittest
import base_login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from object.data import inputValid , inputInvalid  
from object.lockator import elementLogin, adminSearch

class TestLogin(unittest.TestCase):  # test scenario
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_valid_username(self):  
        driver = self.browser
        driver.implicitly_wait(10)
        base_login.test_adminpage(driver)
        
        

    def tearDown(self):
        self.browser.close()
    
if __name__ == "__main__":
    unittest.main()