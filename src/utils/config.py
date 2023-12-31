from typing import Final

from decouple import config


"""
Load values from .env

Сначала сделаем примерный файл на Python с названием 
temp.py и попробуем скрыть в нем пароль.

    userID = 'qwerty'
    password = 'qwerty12345'

    print(userID, password)

Очевидно, что при загрузке этого кода на Github хотелось 
бы, чтобы другие люди не видели пароль, содержащийся 
в файле temp.py

В Python, чтобы скрыть пароль, понадобится функция 
config (она находится в модуле decouple) или функции 
переменных окружения из модуля os. Будем работать с 
функцией config модуля decouple. Для установки этого 
модуля выполняем в терминале следующую команду:

    pip install python-decouple

После установки создаем файл .env в той же папке, 
что и файл test.py, после чего копируем и вставляем 
в него идентификатор пользователя userID и пароль:

    userID = 'qwerty'
    password = 'qwerty12345'

Примечание: этот метод будет работать только при создании 
файла .env. Никакой другой формат файла не подойдет (хотя 
при желании можно использовать .py, .json, .ini или 
config.ini).

Вернемся к файлу test.py и внесем в 
него следующие изменения:

    from decouple import config

    userID = config('userID',default='')
    password = config('password',default='')
    
    print(userID, password)

Проблема по-прежнему остается: любой, кто откроет 
ваш репозиторий, увидит пароль, если откроет файл 
.env. Чтобы не допустить этого, в одной папке с 
.env и test.py создадим файл .gitignore и добавим 
в него .env:

    .env

Github будет игнорировать этот файл .env, так что в 
вашем репозитории его видно не будет. Теперь 
идентификатор пользователя userID и пароль в безопасности.
"""

TOKEN: Final[str] = config('TOKEN', default='')
ADMINS_ID: Final[list] = config('ADMINS_ID', default='')
REDIS_URL: Final[str] = config('REDIS_URL', default='')

DROP_PENDING_UPDATES = True

# DB_PORT: Final[str] = config('', default='')
# DB_HOST: Final[str] = config('', default='')
# DB_NAME: Final[str] = config('', default='')
# DB_USER: Final[str] = config('', default='')
# DB_PASSWORD: Final[str] = config('', default='')

