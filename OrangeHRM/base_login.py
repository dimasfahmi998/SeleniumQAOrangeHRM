import unittest
from object.lockator import elementLogin
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from object.data import inputValid


def test_success_login(driver):  # test cases 1 try this one change
    driver.get(inputValid.baseUrl)
    driver.find_element(By.NAME, elementLogin.username).send_keys(inputValid.username)
    driver.find_element(By.NAME, elementLogin.password).send_keys(inputValid.password)
    driver.find_element(By.CSS_SELECTOR, elementLogin.loginButton).click()
