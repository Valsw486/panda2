from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Указываем путь к geckodriver
driver_path = r'c:\Users\User\.cache\selenium\geckodriver\win64\0.36.0\geckodriver.exe'
service = Service(executable_path=driver_path)

# Создаем драйвер
driver = webdriver.Firefox(service=service)

url = 'https://www.divan.ru/category/divany-i-kresla'

try:
    # Открываем страницу
    driver.get(url)

    # Устанавливаем более длительный таймаут ожидания для загрузки элементов
    wait = WebDriverWait(driver, 30)

    # Ждем появления элементов с ценами
    prices_locator = (By.XPATH, "//span[@data-mark='MainPrice']/span")
    wait.until(EC.presence_of_all_elements_located(prices_locator))

    # Скроллим страницу, чтобы подгрузились все товары (если есть ленивое подгружение)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Можно подождать немного, чтобы контент подгрузился
    wait.until(lambda driver: len(driver.find_elements(*prices_locator)) > 0)

    # Получаем все цены
    prices_elements = driver.find_elements(*prices_locator)

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