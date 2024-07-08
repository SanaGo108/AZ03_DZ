from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv

# Настройка и инициализация драйвера
options = Options()
options.add_argument('--headless')  # Опционально, для работы в фоновом режиме
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

try:
    # Открытие страницы
    driver.get('https://www.divan.ru/category/divany-i-kresla')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.product-card__wrapper')))  # Ожидание загрузки карточек товаров

    # Получение списка карточек товаров
    listings = driver.find_elements(By.CSS_SELECTOR, 'div.product-card__wrapper')

    # Открытие CSV файла для записи
    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Price"])  # Заголовок

        for listing in listings:
            try:
                # Поиск цены внутри карточки
                price = listing.find_element(By.CSS_SELECTOR, 'span.price__main-value')
                cleaned_price = price.text.replace('₽', '').replace(' ', '').strip()  # Очистка строки от символов валюты и пробелов
                writer.writerow([cleaned_price])
                print(cleaned_price)
            except Exception as e:
                print(f"Ошибка при получении цены: {e}")

finally:
    driver.quit()
