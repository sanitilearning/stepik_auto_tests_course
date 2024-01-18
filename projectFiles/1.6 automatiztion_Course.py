#from selenium import webdriver
#from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
#browser.get("http://suninjuly.github.io/simple_form_find_task.html")
#button = browser.find_element(By.ID, "submit_button")

#link = "http://suninjuly.github.io/simple_form_find_task.html"

#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#    button = browser.find_element(By.ID, "submit_button")
#    button.click()

#finally:
#    browser.quit()


#Шаг 4, задача:

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time

#link = "http://suninjuly.github.io/simple_form_find_task.html"

#try:
#    browser = webdriver.Chrome()
#    browser.get(link)

#    input1 = browser.find_element(By.TAG_NAME, "input")
#    input1.send_keys("Ivan")
#    input2 = browser.find_element(By.NAME, "last_name")
#    input2.send_keys("Petrov")
#    input3 = browser.find_element(By.CLASS_NAME, "city")
#    input3.send_keys("Smolensk")
#    input4 = browser.find_element(By.ID, "country")
#    input4.send_keys("Russia")
#    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
 #   button.click()

#finally:
    # успеваем скопировать код за 30 секунд
#    time.sleep(30)
    # закрываем браузер после всех манипуляций
#    browser.quit()

# не забываем оставить пустую строку в конце файла

#Шаг 5

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#import math

#try:
#    link = "http://suninjuly.github.io/find_link_text"

#    browser = webdriver.Chrome()
#    browser.get(link)
#    a = str(math.ceil(math.pow(math.pi, math.e)*10000))
#    link = browser.find_element(By.LINK_TEXT, a)
#    link.click()
#    input1 = browser.find_element(By.TAG_NAME, "input")
#    input1.send_keys("Ivan")
#    input2 = browser.find_element(By.NAME, "last_name")
#    input2.send_keys("Petrov")
#    input3 = browser.find_element(By.CLASS_NAME, "city")
#    input3.send_keys("Smolensk")
#    input4 = browser.find_element(By.ID, "country")
#    input4.send_keys("Russia")
#    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#    button.click()

#finally:
#    time.sleep(30)
#    browser.quit()

#Шаг 6

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time

#try:
#    browser = webdriver.Chrome()
#    browser.get("http://suninjuly.github.io/huge_form.html")
#    elements = browser.find_elements(By.TAG_NAME, "input")
#    for element in elements:
#        element.send_keys("Мой ответ")

#    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#    button.click()

#finally:
    # успеваем скопировать код за 30 секунд
#    time.sleep(30)
    # закрываем браузер после всех манипуляций
#    browser.quit()

# не забываем оставить пустую строку в конце файла

#Шаг 7

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time

#try:
#    browser = webdriver.Chrome()
#    browser.get("http://suninjuly.github.io/find_xpath_form")
#    elements = browser.find_elements(By.TAG_NAME, "input")
#    for element in elements:
#        element.send_keys("Мой ответ")

#    button = browser.find_element(By.XPATH, "Submit")
#    button.click()

#finally:
#    # успеваем скопировать код за 30 секунд
#    time.sleep(30)
    # закрываем браузер после всех манипуляций
#    browser.quit()

#Шаг 8

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time

#link = "https://suninjuly.github.io/find_xpath_form"

#try:
#    browser = webdriver.Chrome()
#    browser.get(link)

#    input1 = browser.find_element(By.NAME, "first_name")
#    input1.send_keys("Ivan")
#    input2 = browser.find_element(By.NAME, "last_name")
#    input2.send_keys("Petrov")
#    input3 = browser.find_element(By.CLASS_NAME, "city")
#    input3.send_keys("Smolensk")
#    input4 = browser.find_element(By.ID, "country")
#    input4.send_keys("Russia")
#    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
#    button.click()

#finally:
    # успеваем скопировать код за 30 секунд
#    time.sleep(30)
    # закрываем браузер после всех манипуляций
#    browser.quit()

# не забываем оставить пустую строку в конце файла. Системы UNIX/Linux ожидают пустую строку в конце файла, если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться.


#Шаг 10 и 11


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
#    link = "http://suninjuly.github.io/registration1.html" #- ссылка, в котором автотест должен успешно работать
    link = "https://suninjuly.github.io/registration2.html" #- ссылка, в котором автотест должен выдавать ошибку NoSuchElementException
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
    input1.send_keys("Anyway1")
    input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//div[@class="form-group second_class"]/input[@class="form-control second"]')
    input2.send_keys("Anyway2")
    input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]//div[@class="form-group third_class"]/input[@class="form-control third"]')
    input3.send_keys("Anyway3")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

