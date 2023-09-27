import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://stepik.org/course/58852/info')
button = browser.find_element(By.XPATH, '//*[@id="ember46"]')
button.click()
time.sleep(5)

input1 = browser.find_element(By.XPATH, '//*[@id="id_registration_full-name"]' )
input1.send_keys('alennester@bk.ru')

time.sleep(5)
browser.quit()