# ====== Messages Doc start ======
"""
Messages are stored in a dictionary, where the key
is the name of the message and the value is its content.

All keys are capitalized as constants
"""
# ======  Messages Doc end  ======


HELLO_MSG = '''Привет, {}
ID: {}

Увы, мне не дали имя, но зато я могу:
▪️ рассказать тебе о проектах, которые мы реализовали
▪️ помочь научиться писать своих ботов
▪️ если ты решил оставить отзыв, с радостью его приму

Выбирай нужный тебе пункт

Если ты хочешь, то можешь придумать мне имя\nкомандой /new_name 😊
'''

MAIN_MENU_MSG = '''Главное меню
после возвращения из подменю
'''

PORTFOLIO_MENU_MSG = '''Меню портфолио с
проектами и все таке
'''

EDUCATION_MENU_MSG = '''Меню с презентацией обучения.
- Приветствие

- Результаты обучения (коротко текстом и где можно посмотреть)

- картинка + текст с кнопками:
--- Программа обучения
--- Отзывы
--- Кто тренер
--- Назад
'''

LEAVE_FEEDBACK_MSG = '''
Здесь нужна инструкция для того, 
чтобы юзер мог через бота написать и отзыв
опубликуется в канал с отзывами. После чего юзеру
придет спасибо-сообщение с ссылкой на побликацию
и вообще перед отправкой нужно подтверждение и 
фильтр слов
'''

WRITE_TO_PRIVATE_MSG = '''
Включен режим диалога с администратором. 

Вы можете написать сообщение и в течение 5-55 минут вам ответят.
Спасибо за ожидание.
'''


MSG = {
    'HELLO':                HELLO_MSG,
    'MAIN_MENU':            MAIN_MENU_MSG,
    'PORTFOLIO_MENU':       PORTFOLIO_MENU_MSG,
    'EDUCATION_MENU':       EDUCATION_MENU_MSG,
    'LEAVE_FEEDBACK':       LEAVE_FEEDBACK_MSG,
    'WRITE_TO_PRIVATE_MSG': WRITE_TO_PRIVATE_MSG,
}



# ====== Logs Doc start ======
""" 
There is no documentation for the logo
"""
# ======  Logs Doc end  ======

LOGS = {}


"""ADMIN MENU"""

ADMIN_MSG = {}


# ====== Keyboard Doc start ======
"""
To learn more about the parameters of 
constants, go to the keyboard constructor:

src/keyboard/inline/constructor.py

Template for creating data for keyboards:

KEYBOARD = {
    'btns_count':    4,
    'keyboard_view': 'column',
    'buttons_data':  [
        {'name': '', 'callback': 'go_to_ ...'},
        ... ,
    ]
}
"""
# ======  Keyboard Doc end  ======

MAIN_KB = {
    'btns_count':    4,
    'keyboard_view': 'column',
    'buttons_data':  [
        {'name': 'Портфолио ботов', 'callback': 'go_to_portfolio'},
        {'name': 'Обучение', 'callback': 'go_to_education'},
        {'name': 'Оставить отзыв', 'callback': 'go_to_write_feedback'},
        {'name': 'Написать в лс', 'callback': 'go_to_write_private'},
    ]
}

PORTFOLIO_KB = {
    'btns_count':    4,
    'keyboard_view': 'shop_cards',
    'buttons_data':  [
        {'name': '◀️', 'callback': 'go_to_prev_proj'},
        {'name': 'Открыть', 'callback': 'go_to_inside_proj'},
        {'name': '▶️', 'callback': 'go_to_write_next_proj'},
        {'name': 'Назад', 'callback': 'go_to_main_menu'},
    ]
}

PROJECT_KB = {
    'btns_count':    1,
    'keyboard_view': 'column',
    'buttons_data':  [
        {'name': 'Назад', 'callback': 'go_to_portfolio'},
    ]
}
