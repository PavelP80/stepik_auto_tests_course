from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    '''
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    print(os.path.dirname(__file__))
'''
    
    x = browser.find_element(By.CSS_SELECTOR,"#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x)
    x=x.text
    print("x= ",x)
    yx = calc(x)
    print("yx= ",yx)
  

    browser.find_element(By.CSS_SELECTOR,"#answer").send_keys(yx)
    browser.find_element(By.CSS_SELECTOR,"#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR,"#robotsRule").click()
    button = browser.find_element(By.XPATH,"//button[text()='Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла