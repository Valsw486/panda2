from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Путь к geckodriver
driver_path = r'c:\Users\User\.cache\selenium\geckodriver\win64\0.36.0\geckodriver.exe'
service = Service(executable_path=driver_path)

# Создаем драйвер
driver = webdriver.Firefox(service=service)

url = 'https://www.divan.ru/category/divany-i-kresla'

try:
    driver.get(url)

    wait = WebDriverWait(driver, 60)  # увеличиваем таймаут

    # Прокрутка страницы вниз с проверкой, что страница достигла конца
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # подождать, чтобы контент подгрузился
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Ждем появления цен
    prices_locator = (By.XPATH, "//span[@data-mark='MainPrice']/span")
    wait.until(EC.presence_of_all_elements_located(prices_locator))

    # Получаем цены
    prices_elements = driver.find_elements(*prices_locator)
    prices = [price.text for price in prices_elements]

    # Запись в CSV
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