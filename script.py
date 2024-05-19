import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Проверка доступа к интернету


def check_internet_connection():
    try:
        subprocess.check_call(
            ["ping", "-c", "5", "google.com"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False


# Основная логика скрипта
if check_internet_connection():
    # Настройка Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Запуск ChromeDriver
    driver = webdriver.Chrome(service=Service(
        "/usr/local/bin/chromedriver"), options=chrome_options)

    # Открытие сайта
    driver.get("https://insdo.rea.ru/login/index.php")

    # Ожидание появления кнопки логина
    wait = WebDriverWait(driver, 15)
    login_button = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "Войти с помощью ЭИОС"))
    )
    login_button.click()

    # Ввод логина и пароля
    driver.find_element(By.ID, "login").send_keys(os.getenv("LOGIN"))
    driver.find_element(By.ID, "password").send_keys(os.getenv("PASSWORD"))
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Поиск и воспроизведение видео
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "video")))
    videos = driver.find_elements(By.TAG_NAME, "video")
    for video in videos:
        driver.execute_script("return arguments[0].play();", video)
        time.sleep(15)  # Ждать 15 секунд воспроизведения видео

    driver.quit()
else:
    print("Нет доступа к интернету. Пожалуйста, проверьте подключение.")
