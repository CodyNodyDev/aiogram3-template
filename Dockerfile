FROM python:3.10.12

WORKDIR /aiogram3-template

COPY ./requirements.txt ./

# Устанавливаем зависимости и gunicorn

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r ./requirements.txt


# Укажите команду, которая будет выполняться при запуске контейнера
CMD ["python3", "src/main.py"]

