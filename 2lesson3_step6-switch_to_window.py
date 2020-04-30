'''
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
'''

from selenium import webdriver
import time
import math 
from selenium.webdriver.support.ui import Select

try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

#Нажимаем кнопку
    button = browser.find_element_by_css_selector('.btn')
    button.click()

#Переходим на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

#Математическая функция
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

#Находим на странице x и подставляем в функцию
    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)

 #Выводим результат в нужное поле
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

#Нажимаем кнопку
    button = browser.find_element_by_css_selector('.btn')
    button.click() 

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

