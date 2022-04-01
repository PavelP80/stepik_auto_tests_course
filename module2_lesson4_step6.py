from selenium import webdriver
from selenium.webdriver.common.by import By

import time 


try:


	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/cats.html")
	browser.implicitly_wait(5)

	button = browser.find_element(By.ID,"button")
	button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла