FROM python:3.10.12

# Install necessary build dependencies, including libyaml-dev
RUN apt-get update && apt-get install -y libyaml-dev

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Устанавливаем рабочую директорию в контейнере
WORKDIR /usr/src/app

# Копируем файлы зависимостей в рабочую директорию
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в рабочую директорию
COPY ./src /usr/src/app

# Задаем команду для запуска приложения
CMD ["python", "./main.py"]