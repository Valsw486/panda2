from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
import time
import re
import csv



driver = webdriver.Firefox()

# URL первой страницы каталога диванов
base_url = 'https://www.divan.ru/category/divany-i-kresla'

prices = []

try:
    driver.get(base_url)
    time.sleep(3)  # подождать загрузки страницы

    # Можно прокрутить страницу, чтобы подгрузились все товары, если есть lazy load
    # например, с помощью execute_script
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Получить список карточек товаров
    product_cards = driver.find_elements(By.CLASS_NAME, 'catalog-item')  # уточните класс

    for card in product_cards:
        try:
            price_element = card.find_element(By.CLASS_NAME, 'price')  # уточните класс
            price_text = price_element.text
            # Извлечь число из текста цены
            price_numbers = re.findall(r'\d+', price_text)
            if price_numbers:
                price_value = int(''.join(price_numbers))
                prices.append(price_value)
        except:
            continue

finally:
    driver.quit()

# Сохраняем цены в CSV
df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('divan_prices.csv', index=False)

# Обработка данных: нахождение средней цены
if len(prices) > 0:
    average_price = sum(prices) / len(prices)
    print(f'Средняя цена на диваны: {average_price:.2f}')
else:
    print('Цены не найдены.')

# Построение гистограммы
# plt.hist(prices, bins=20, edgecolor='black')
# plt.title('Гистограмма цен на диваны')
# plt.xlabel('Цена')
# plt.ylabel('Количество')
# plt.show()