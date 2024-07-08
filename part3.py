# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать
# данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны

import csv
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_service = Service()

# Инициализация веб-драйвера
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Открытие сайта
driver.get('https://www.divan.ru/')

# Подождем, пока страница полностью загрузится
time.sleep(5)

# Пример парсинга данных о диванах
products = driver.find_elements(By.CLASS_NAME, 'product-card__info')  # Найти все карточки продуктов

data = []

for product in products:
    try:
        name = product.find_element(By.CLASS_NAME, 'product-card__title').text
        price = product.find_element(By.CLASS_NAME, 'product-card__price').text
        data.append([name, price])
    except:
        continue

# Закрытие веб-драйвера
driver.quit()

# Запись данных в CSV файл
with open('divan_prices.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price'])  # Заголовки столбцов
    writer.writerows(data)

print("Данные успешно сохранены в divan_prices.csv")

# Загружаем CSV файл
df = pd.read_csv('divan_prices.csv')

# Предположим, что интересующие нас данные находятся в колонке 'price'
# Удаляем '₽/мес.' и преобразуем в тип данных float
df['price'] = df['price'].str.replace('₽/мес.', '', regex=False).str.replace(' ', '').astype(float)

# Сохраняем измененный DataFrame обратно в CSV файл
df.to_csv('your_file_processed.csv', index=False)