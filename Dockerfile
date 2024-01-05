FROM python:3.10.12

# Обновляем список пакетов и устанавливаем зависимости для pycups
RUN apt-get update && apt-get install -y \
    gcc \
    libcups2-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию в контейнере
WORKDIR /usr/app/src

# Копируем файлы зависимостей в рабочую директорию
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в рабочую директорию
COPY ./src /usr/app/src

# Задаем команду для запуска приложения
CMD ["python", "./main.py"]