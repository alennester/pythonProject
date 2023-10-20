import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def set_up():
    link = 'https://www.saucedemo.com/'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()
    yield
 
def test_mail_1_09(set_up):
    browser.close()
    user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    user_name.send_keys('standard_user')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('secret_sauce')

    button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    button_login.click()

def test_mail_1_09(set_up):
    pass
def test_mail_1_09(set_up):
    pass
def test_mail_1_09(set_up):
    pass
