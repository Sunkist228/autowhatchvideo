# Использовать базовый образ Python
FROM python:3.9-slim

# Установка зависимостей Google Chrome
RUN apt-get update && apt-get install -y \
	fonts-liberation \
	libasound2 \
	libatk-bridge2.0-0 \
	libatk1.0-0 \
	libcups2 \
	libdrm2 \
	libgbm1 \
	libnspr4 \
	libnss3 \
	libx11-xcb1 \
	libxcomposite1 \
	libxdamage1 \
	libxrandr2 \
	wget \
	--no-install-recommends && \
	rm -rf /var/lib/apt/lists/*

# Скачивание файлов ChromeDriver и Google Chrome из директорий проекта
COPY src/chromedriver_linux64.zip /tmp/chromeDriver.zip
COPY src/google-chrome-stable_current_amd64-107.0.5304.63.deb /tmp/google-chrome.deb

# Установка ChromeDriver
RUN unzip /tmp/chromeDriver.zip -d /usr/local/bin

# Установка Google Chrome
RUN dpkg -i /tmp/google-chrome.deb && apt-get install -f -y

# Копирование остальных файлов проекта
COPY . /app
WORKDIR /app

# Запуск скрипта
CMD ["python", "script.py"]
