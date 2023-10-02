import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link ='http://suninjuly.github.io/execute_script.html'
browser= webdriver.Chrome()
browser.get(link)
browser.maximize_window()

x = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x.text
y = calc(x)


button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

string = browser.find_element(By.XPATH, '//*[@id="answer"]')
string.send_keys(y)

check = browser.find_element(By.XPATH,'/html/body/div/form/div[2]/label')
check.click()

radiobutton = browser.find_element(By.XPATH, '/html/body/div/form/div[4]/label')
radiobutton.click()

button = browser.find_element(By.XPATH, '/html/body/div/form/button')
button.click()


time.sleep(15)
browser.quit()