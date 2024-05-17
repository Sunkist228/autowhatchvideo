import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Проверка доступа к интернету


def check_internet_connection():
    try:
        # Попытка выполнить ping на google.com
        subprocess.run(
            ["ping", "-c", "5", "lmsdo.rea.ru/login/index.php"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False


# Если есть доступ к интернету, выполняем скрипт Selenium
if check_internet_connection():
    # Настройки Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Запуск ChromeDriver
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Открытие сайта
    driver.get(
        '< class="btn btn-primary unti-login-button" href="https://lmsdo.rea.ru/login/index.php')

    # Ожидание появления кнопки логина в течение 10 секунд
    wait = WebDriverWait(driver, 15)
    login_button = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "Войти с помощью “20.35”")))

    # Клик по кнопке логина
    login_button.click()

    # Ввод логина и пароля
    driver.find_element(By.ID, 'login').send_keys('egor.k.s@mail.ru')
    driver.find_element(By.ID, 'password').send_keys('QX64LanY2CkfY8Nx')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    time.sleep(15)  # Подождите, пока выполнится вход

    # Найдите все видео и просмотрите их полностью
    videos = driver.find_elements(By.TAG_NAME, 'video')
    for video in videos:
        duration = driver.execute_script(
            "return arguments[0].duration;", video)
        driver.execute_script("arguments[0].play();", video)
        time.sleep(duration)  # Ждать продолжительность видео

    driver.quit()
else:
    print("Нет доступа к интернету. Пожалуйста, проверьте подключение.")
