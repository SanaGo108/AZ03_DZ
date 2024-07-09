import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

chrome_options = Options()
# Инициализация драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Открытие страницы
    driver.get('https://www.divan.ru/category/divany-i-kresla')
    time.sleep(5)  # Ждать загрузки страницы

    # Поиск всех объявлений на странице
    listings = driver.find_elements(By.XPATH, '//div[@.wDTtf"]')

    for listing in listings:
        try:
            # Поиск цены внутри объявления
            price = listing.find_element(By.XPATH, './/span[@.ui-LD-ZU.KIkOH]')
            print(price.text)
        except Exception as e:
            print(f"Ошибка при получении цены: {e}")

  # Открытие CSV файла для записи
    with open('divan_prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Price"])  # Запись заголовка

        for listing in listings:
            try:
                # Поиск цены внутри объявления
                price = listing.find_element(By.XPATH, './/span[@data-mark="MainPrice"]')
                writer.writerow([price.text])  # Запись цены в CSV файл
            except Exception as e:
                print(f"Ошибка при получении цены: {e}")

finally:
    # Закрытие драйвера
    driver.quit()