from selenium import webdriver
from selenium.webdriver.common.by import By

import time 

import os




try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    browser.find_element(By.NAME,"firstname").send_keys("Vasya")
    browser.find_element(By.NAME,"lastname").send_keys("Pupkin")
    browser.find_element(By.NAME,"email").send_keys("Vasya@pupkin.com")
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'module2_lesson2_step8.txt')           # добавляем к этому пути имя файла 
    browser.find_element(By.ID,"file").send_keys(file_path)
    
    button = browser.find_element(By.XPATH,"//button[text()='Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла