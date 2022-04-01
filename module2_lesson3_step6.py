from selenium import webdriver
from selenium.webdriver.common.by import By

import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    
    browser.find_element(By.CSS_SELECTOR,"button.trollface").click()
    
    browser.switch_to.window(browser.window_handles[1])
    
    
    x=browser.find_element(By.ID,"input_value").text
    print ("x = ",x)
    y=calc(int(x))
    
    x=browser.find_element(By.ID,"answer").send_keys(y)

 
    browser.find_element(By.XPATH,"//button[text()='Submit']").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла