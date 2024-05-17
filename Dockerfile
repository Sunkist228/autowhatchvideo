FROM python:3.9-slim

RUN pip install selenium

RUN apt-get update && apt-get install -y \
	wget \
	unzip \
	gnupg \
	xvfb \
	iputils-ping && \
	rm -rf /var/lib/apt/lists/*

# Установка зависимостей Google Chrome
RUN apt-get update && apt-get install -y \
	fonts-liberation \
	libasound2 \
	libatk-bridge2.0-0 \
	libatk1.0-0 \
	libatspi2.0-0 \
	libcairo2 \
	libcups2 \
	libcurl3-gnutls \
	libdbus-1-3 \
	libgbm1 \
	libglib2.0-0 \
	libgtk-3-0 \
	libnspr4 \
	libnss3 \
	libpango-1.0-0 \
	libwayland-client0 \
	libxcomposite1 \
	libxdamage1 \
	libxkbcommon0 \
	xdg-utils --no-install-recommends && \
	rm -rf /var/lib/apt/lists/*

# Копирование файлов ChromeDriver и Google Chrome из директории проекта
COPY src/chromedriver_linux64.zip /tmp/chromedriver.zip
COPY src/google-chrome-stable_current_amd64-107.0.5304.63.deb /tmp/google-chrome.deb

# Установка ChromeDriver
RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/

# Установка Google Chrome
RUN dpkg -i /tmp/google-chrome.deb && apt-get install -f -y

# Копирование остальных файлов проекта
COPY . /app
WORKDIR /app

CMD ["python", "script.py"]
