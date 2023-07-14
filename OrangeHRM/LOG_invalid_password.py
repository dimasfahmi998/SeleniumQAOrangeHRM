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

    def test_login_invalid_password(self):  
        driver = self.browser

        driver.get(inputValid.baseUrl)
        driver.implicitly_wait(10)
        driver.find_element(By.NAME, elementLogin.username).send_keys(inputValid.username)
        driver.find_element(By.NAME, elementLogin.password).send_keys(inputInvalid.password)
        driver.find_element(By.CSS_SELECTOR, elementLogin.loginButton).click()
        assert driver.find_element(By.CSS_SELECTOR, elementLogin.invalidLogin).text == inputInvalid.textInvalidLogin

    def tearDown(self):
        self.browser.close()
    
if __name__ == "__main__":
    unittest.main()
