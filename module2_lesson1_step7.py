from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR,"#treasure").get_attribute("valuex")
    
    #x = x_element.text
    x = x_element
    print("x= ",x)
    y = calc(x)
    print("y= ",y)
    
    browser.find_element(By.CSS_SELECTOR,"#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR,"#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR,"#robotsRule").click()
    browser.find_element(By.XPATH,"//button[text()='Submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла