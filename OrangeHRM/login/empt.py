import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from object.data import inputValid , inputInvalid
from object.lockator import elementLogin

class TestLogin(unittest.TestCase):  # test scenario
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_login_empty(self):  
        driver = self.browser

        driver.get(inputValid.baseUrl)
        driver.implicitly_wait(50)
        driver.find_element(By.CSS_SELECTOR, elementLogin.loginButton).click()
        assert driver.find_element(By.CSS_SELECTOR, elementLogin.RequiredUsername).text == inputInvalid.textEmpty
        assert driver.find_element(By.CSS_SELECTOR, elementLogin.RequiredPassword).text == inputInvalid.textEmpty
        
    def tearDown(self):
        self.browser.close()
    
if __name__ == "__main__":
    unittest.main()