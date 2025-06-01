from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Указываем путь к geckodriver
driver_path = r'c:\Users\User\.cache\selenium\geckodriver\win64\0.36.0\geckodriver.exe'
service = Service(executable_path=driver_path)

# Создаем драйвер с помощью service
driver = webdriver.Firefox(service=service)



url ='https://www.divan.ru/category/divany-i-kresla'

try:
    # Открытие страницы
    driver.get(url)

    time.sleep(5)

    # Явное ожидание, чтобы убедиться, что страница полностью загрузилась
    wait = WebDriverWait(driver, 15)
    # Подождем, пока не появится элемент с ценами
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-mark='MainPrice']/span")))

    # Скроллим страницу, чтобы подгрузились все товары (если есть ленивое подгружение)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Немного подождем после скролла

    # Получаем все цены
    prices_elements = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

    # Собираем цены в список
    prices = [price.text for price in prices_elements]

    # Записываем в CSV
    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])
        for price in prices:
         writer.writerow([price])

         print("Цены успешно записаны в prices.csv")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
        driver.quit()

