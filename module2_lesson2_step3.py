﻿from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(num1,num2):
  return str(int(num1)+int(num2))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element(By.CSS_SELECTOR,"#num1").text
    print("x= ",x)
    y= browser.find_element(By.CSS_SELECTOR,"#num2").text
    print("y= ",y)
    yx = calc(x,y)
    
    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_visible_text(yx) # ищем элемент с текстом "Python"
    browser.find_element(By.XPATH,"//button[text()='Submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла