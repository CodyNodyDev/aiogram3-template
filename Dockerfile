FROM python:3.10.12


COPY .requirements.txt .

COPY . .

WORKDIR /app

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Укажите команду, которая будет выполняться при запуске контейнера
CMD ["python3", "src/main.py"]

