import time
from selenium import webdriver
from selenium.webdriver.common.by import By

button = browser.find_element(By.XPATH,'//*[@id="ember27"]')
button.click()

mail = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
mail.send_keys('Alen')

l_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
l_name.send_keys('Nester')

