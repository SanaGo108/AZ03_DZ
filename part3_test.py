from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv

# Настройка драйвера Chrome
chrome_options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = selenium.webdriver.support.ui.WebDriverWait(driver, 10)  # Явное ожидание

try:
    # Переход на страницу с диванами
    driver.get('https://www.divan.ru/category/divany-i-kresla')

    # Ожидание загрузки элементов с ценами
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.product-card__wrapper div.product-card__prices span.price__main-value')))

    # Сбор информации о ценах
    products = driver.find_elements(By.CSS_SELECTOR, 'div.product-card__wrapper div.product-card__prices span.price__main-value')
    prices = [p.text.strip() for p in products if p.text]

    print(f"Найдено цен: {len(prices)}")  # Логирование количества найденных элементов

    # Сохранение данных в CSV
    with open('divan_prices.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])
        for price in prices:
            writer.writerow([price.replace(' ₽', '').replace(' ', '')])

finally:
    driver.quit()

print("Данные успешно сохранены.")
