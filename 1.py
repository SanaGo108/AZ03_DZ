import selenium
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# Инициализация драйвера
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

try:
    # Открытие страницы
    driver.get('https://www.divan.ru/category/divany-i-kresla')

    # Ожидание загрузки страницы и наличия объявлений
    element = wait.until(EC.presence_of_element_located((By.ID, 'element_id')))
    listings = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-name="LinkArea"]')))

    # Открытие CSV файла для записи
    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Price"])  # Запись заголовка

        for listing in listings:
            try:
                # Поиск цены внутри объявления
                price = listing.find_element(By.XPATH, './/span[@data-mark="MainPrice"]')
                writer.writerow([price.text])  # Запись цены в CSV файл
                print(price.text)  # Вывод цены на экран
            except Exception as e:
                print(f"Ошибка при получении цены: {e}")

finally:
    # Закрытие драйвера
    driver.quit()