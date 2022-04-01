from selenium import webdriver
from selenium.webdriver.common.by import By

import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.CSS_SELECTOR,"button.btn").click()
    
    print("WTF? ",browser.switch_to.alert.text)
    browser.switch_to.alert.accept()
    
    x=browser.find_element(By.ID,"input_value").text
    print ("x = ",x)
    y=calc(int(x))
    
    x=browser.find_element(By.ID,"answer").send_keys(y)

 
    button = browser.find_element(By.XPATH,"//button[text()='Submit']")
       
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла