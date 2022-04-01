﻿from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.CSS_SELECTOR,"div .first_block .first_class input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR,"div .first_block .second_class input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR,"div .first_block .third_class input")
    input3.send_keys("email@email.com")
    #input4 = browser.find_element(By.ID,"country")
    #input4.send_keys("Russia")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME,"h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    print("##########################")
    print(welcome_text)
    print("##########################")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла