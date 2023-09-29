import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try: 
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    print(y)

    answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer.send_keys(y)

    check = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/label')
    check.click()

    radio = browser.find_element(By.XPATH, '/html/body/div/form/div[4]/label')
    radio.click()

    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()