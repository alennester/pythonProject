import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
try:
    link ='http://suninjuly.github.io/file_input.html'
    browser= webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    f_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
    f_name.send_keys('Alen')

    l_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
    l_name.send_keys('Nester')

    mail = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
    mail.send_keys('alenneste@bk.ru')

    element = browser.find_element(By.XPATH, '//*[@id="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'fil.txt')
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH,'/html/body/div/form/button')
    button.click()
finally:
    time.sleep(10)
    browser.quit()