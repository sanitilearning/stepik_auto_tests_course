#Урок 1.6, Шаг 11 - Задание: уникальность селекторов, ссылка https://stepik.org/lesson/138920/step/11?unit=196194
#Отправляю решение задания на проверку

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