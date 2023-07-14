import unittest
from object.lockator import elementLogin , adminSearch ,PIMmenu
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from object.data import inputValid


def test_adminpage(driver):

    driver.get(inputValid.baseUrl)
    driver.implicitly_wait(50)
    driver.find_element(By.NAME, elementLogin.username).send_keys(inputValid.username)
    driver.find_element(By.NAME, elementLogin.password).send_keys(inputValid.password)
    driver.find_element(By.CSS_SELECTOR, elementLogin.loginButton).click()
    driver.find_element(By.CSS_SELECTOR, adminSearch.sidebarAdmin).click()

def test_pimpage(driver):

    driver.get(inputValid.baseUrl)
    driver.implicitly_wait(50)
    driver.find_element(By.NAME, elementLogin.username).send_keys(inputValid.username)
    driver.find_element(By.NAME, elementLogin.password).send_keys(inputValid.password)
    driver.find_element(By.CSS_SELECTOR, elementLogin.loginButton).click()
    driver.find_element(By.LINK_TEXT, PIMmenu.sidebarPIM).click()
