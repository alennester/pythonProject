import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try: 
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    box = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = box.get_attribute('valuex')
    y = calc(x)

    answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer.send_keys(y)

    check = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    check.click()

    radio = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    radio.click()

    button = browser.find_element(By.XPATH, '/html/body/div/form/div/div/button')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
