import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.maximize_window()

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = browser.find_element(By.XPATH, '//*[@id="book"]')
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
button.click()

x = browser.find_element(By.XPATH,'//*[@id="input_value"]')
y = calc(x)

input1 = browser.find_element(By.XPATH,'//*[@id="answer"]')
input1.send_keys(y)

button2 = browser.find_element(By.XPATH, '//*[@id="solve"]')
button2.click()

time.sleep(15)
browser.quit()