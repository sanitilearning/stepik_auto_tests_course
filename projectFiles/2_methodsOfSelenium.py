#Урок 2.1, Шаг 5
#import time

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#import math

#try:
#    link = "https://suninjuly.github.io/math.html"
#    browser = webdriver.Chrome()
#    browser.get(link)


#    def calc(x):
#        return str(math.log(abs(12 * math.sin(int(x)))))
#    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
#    x = x_element.text
#    y = calc(x)

#    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
#    input1.send_keys(y)
#    time.sleep(1)

#    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
#    option1.click()
#    time.sleep(1)
#    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
#    option2.click()
#    time.sleep(1)
#    option3 = browser.find_element(By.CLASS_NAME, "btn")
#    option3.click()
#finally:
#    time.sleep(10)
#    browser.quit()


#Урок 2.1, Шаг 7


#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#import math

#link = "http://suninjuly.github.io/get_attribute.html"
#browser = webdriver.Chrome()
#browser.get(link)


#def calc(x):
#   return str(math.log(abs(12 * math.sin(int(x)))))
#x_element = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
#x = x_element.get_attribute("valuex")
#y = calc(x)
#print(x)
#input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
#input1.send_keys(y)
#time.sleep(1)

#option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
#option1.click()
#time.sleep(1)
#option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
#option2.click()
#time.sleep(1)
#option3 = browser.find_element(By.CLASS_NAME, "btn")
#option3.click()

#time.sleep(10)
#browser.quit()


#Урок 2.2 Работа с файлами, списками и js-скриптами, Шаг 2.3


#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#import math
#from selenium.webdriver.support.ui import Select

#link = "http://suninjuly.github.io/selects1.html"
#browser = webdriver.Chrome()
#browser.get(link)

#def calc(x1, x2):
#    return str(str(int(x1) + int(x2)))
#x_element1 = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
#x1 = x_element1.text
#x_element2 = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
#x2 = x_element2.text
#y = calc(x1, x2)

#select = Select(browser.find_element(By.TAG_NAME, "select"))
#select.select_by_value(y) # ищем элемент, значение которого совпадает со значением переменной y

#option_button = browser.find_element(By.CLASS_NAME, "btn")
#option_button.click()

#time.sleep(10)
#browser.quit()


#Шаг 5

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time

#browser = webdriver.Chrome()
#link = "https://SunInJuly.github.io/execute_script.html"
#browser.get(link)
#button = browser.find_element(By.TAG_NAME, "button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()

#time.sleep(10)


#Шаг6

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#import math
#from selenium.webdriver.support.ui import Select

#link = "http://suninjuly.github.io/execute_script.html"
#browser = webdriver.Chrome()
#browser.get(link)

#def calc(x):
#    return str(math.log(abs(12 * math.sin(int(x)))))
#x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
#x = x_element.text
#y = calc(x)

#browser.execute_script("window.scrollBy(0, 100);")
#button = browser.find_element(By.ID, "answer")
#button.send_keys(y)

#checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
#checkbox.click()
#radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
#radiobutton.click()

#option_button = browser.find_element(By.CLASS_NAME, "btn")
#option_button.click()

#time.sleep(10)
#browser.quit()


#Шаг 8


#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import os
#import time

#link = "http://suninjuly.github.io/file_input.html"
#browser = webdriver.Chrome()
#browser.get(link)




#option1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
#option1.send_keys("Alex")
#option2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
#option2.send_keys("Learning")
#option3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
#option3.send_keys("rus.com")

#current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
#file_path = os.path.join(current_dir, 'new_file.txt')           # добавляем к этому пути имя файла
#option_load = browser.find_element(By.CSS_SELECTOR, "[id='file']")
#option_load.send_keys(file_path)

#option_button = browser.find_element(By.CLASS_NAME, "btn")
#option_button.click()

#time.sleep(10)
#browser.quit()


#Урок 2.3, Шаг 4


#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import math
#import time

#link = "http://suninjuly.github.io/alert_accept.html"
#browser = webdriver.Chrome()
#browser.get(link)

#button1 = browser.find_element(By.CLASS_NAME, "btn-primary")
#button1.click()
#confirm = browser.switch_to.alert
#confirm.accept()

#def calc(x):
#    return str(math.log(abs(12*math.sin(int(x)))))
#element_x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
#x = element_x.text
#y = calc(x)

#answer_field = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
#answer_field.send_keys(y)

#button2 = browser.find_element(By.CLASS_NAME, "btn-primary")
#button2.click()

#time.sleep(10)
#browser.quit()


#Шаг 6


#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import math
#import time

#link = "http://suninjuly.github.io/redirect_accept.html"
#browser = webdriver.Chrome()
#browser.get(link)

#button1 = browser.find_element(By.CLASS_NAME, "trollface")
#button1.click()
#first_window = browser.window_handles[0]
#new_window = browser.window_handles[1]
#browser.switch_to.window(new_window)

#def calc(x):
#    return str(math.log(abs(12*math.sin(int(x)))))
#element_x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
#x = element_x.text
#y = calc(x)

#answer_field = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
#answer_field.send_keys(y)

#button2 = browser.find_element(By.CLASS_NAME, "btn-primary")
#button2.click()

#time.sleep(10)
#browser.quit()


#Урок 2.4, Шаг 3-4

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time

#browser = webdriver.Chrome()
#browser.get("http://suninjuly.github.io/wait1.html")

#time.sleep(1)
#button = browser.find_element(By.ID, "verify")
#button.click()
#message = browser.find_element(By.ID, "verify_message")

#assert "successful" in message.text



#Урок 2.4, Шаг 5

#from selenium import webdriver
#from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
#browser.implicitly_wait(5)

#browser.get("http://suninjuly.github.io/wait1.html")

#button = browser.find_element(By.ID, "verify")
#button.click()
#message = browser.find_element(By.ID, "verify_message")

#assert "successful" in message.text


#Шаг 6

#from selenium import webdriver
#from selenium.webdriver.common.by import By

#browser = webdriver.Chrome()
#говорим WebDriver искать каждый элемент в течение 5 секунд
#browser.implicitly_wait(5)

#browser.get("http://suninjuly.github.io/wait1.html")
#browser.find_element(By.ID, "button")


#Шаг 7


#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver

#browser = webdriver.Chrome()

#browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#button = WebDriverWait(browser, 5).until(
#        EC.element_to_be_clickable((By.ID, "verify"))
#    )
#button.click()
#message = browser.find_element(By.ID, "verify_message")

#assert "successful" in message.text


#Шаг 8


#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver
#import math
#import time

#browser = webdriver.Chrome()

#browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
#find_price = (WebDriverWait(browser, 25).until(
#              EC.text_to_be_present_in_element((By.ID, "price"), "100"))
#    )
#button = browser.find_element(By.ID, "book")
#button.click()

#def calc(x):
#    return str(math.log(abs(12*math.sin(int(x)))))
#element_x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
#x = element_x.text
#y = calc(x)

#field_answer = browser.find_element(By.ID, "answer")
#field_answer.send_keys(y)
#submit_button = browser.find_element(By.ID, "solve")
#submit_button.click()

#time.sleep(10)
#browser.quit()

