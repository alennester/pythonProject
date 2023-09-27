import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://stepik.org/catalog')
browser.maximize_window()
time.sleep(3)

login = browser.find_element(By.XPATH, '//*[@id="ember245"]')
login.click()

user_name = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
user_name.send_keys('alennester@bk.ru')

parol = browser.find_element(By.XPATH, '//*[@id="id_login_password"]')
parol.send_keys('alennester@bk.ru')

button = browser.find_element(By.XPATH, '//*[@id="login_form"]/button')
button.click()

time.sleep(5)
browser.quit()