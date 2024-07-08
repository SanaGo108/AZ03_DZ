from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Укажите путь к вашему chromedriver
path_to_chromedriver = 'path_to_chromedriver'

# Инициализация сервиса с указанием пути к chromedriver
service = Service(executable_path=path_to_chromedriver)

# Инициализация драйвера с использованием объекта сервиса
driver = webdriver.Chrome(service=service)

# Открываем страницу
driver.get('http://example.com')

# Инициализация WebDriverWait с использованием объекта driver и времени ожидания в секундах
wait = WebDriverWait(driver, 10)

# Ожидание появления элемента с ID 'element_id'
try:
    element = wait.until(EC.presence_of_element_located((By.ID, 'element_id')))
    print("Element found!")
except Exception as e:
    print(f"An error occurred: {e}")

# Не забудьте закрыть драйвер после завершения работы
driver.quit()