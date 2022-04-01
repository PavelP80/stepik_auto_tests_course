
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time 
import math
import os

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:


	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	browser.implicitly_wait(5)


	button=browser.find_element(By.ID,"book")
	price=WebDriverWait(browser, 12).until(
	        EC.text_to_be_present_in_element((By.ID, "price"),"100")
	        	    )
	button.click()

	x=browser.find_element(By.ID,"input_value").text
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	print ("x = ", x)
	y=calc(x)
	print ("y = ", y)
	
	browser.find_element(By.ID,"answer").send_keys(y)
	browser.find_element(By.ID,"solve").click()
	


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()
    
# не забываем оставить пустую строку в конце файла