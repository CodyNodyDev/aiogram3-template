# ====== Messages Doc start ======
"""
Messages are stored in a dictionary, where the key
is the name of the message and the value is its content.

All keys are capitalized as constants
"""
# ======  Messages Doc end  ======


HELLO_MSG = '''Привет, {}
ID: {}

Hello message 😊
'''

MAIN_MENU_MSG = '''Главное меню
MAIN MENU DESCRIPTION
'''

PORTFOLIO_MENU_MSG = '''Меню портфолио
PORTFOLIO DESCRIPTION
'''

EDUCATION_MENU_MSG = '''Меню с презентацией обучения
EDUCATION MENU DESCRIPTION
'''

LEAVE_FEEDBACK_MSG = '''
FEEDBACK MENU - disabled
'''

WRITE_TO_PRIVATE_MSG = '''STATE MODE DEMONSTRATION
Включен режим диалога с администратором. 

Напишите сообщение и в ближайшее время администратор ответит.

Если вы хотите завершить диалог, нажимите на кнопку
'''

USER_TIP_FOR_DIALOG = '''Ответ:\n{}\n\nЧтобы завершить диалог, нажмите на кнопку или продолжайте переписку'''

END_DIALOG_MODE = ''''Режим диалога завершен'''

MSG = {
    'HELLO':                HELLO_MSG,
    'MAIN_MENU':            MAIN_MENU_MSG,
    'PORTFOLIO_MENU':       PORTFOLIO_MENU_MSG,
    'EDUCATION_MENU':       EDUCATION_MENU_MSG,
    'LEAVE_FEEDBACK':       LEAVE_FEEDBACK_MSG,
    'WRITE_TO_PRIVATE_MSG': WRITE_TO_PRIVATE_MSG,
    'USER_TIP_FOR_DIALOG':  USER_TIP_FOR_DIALOG,
    'END_DIALOG_MODE':      END_DIALOG_MODE,
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
        {'name': 'Портфолио', 'callback': 'go_to_portfolio'},
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

END_DIALOG_MODE_KB = {
    'btns_count': 1,
    'keyboard_view': 'column',
    'buttons_data': [
        {'name': 'Завершить диалог', 'callback': 'finish_to_write_private'},
    ]
}

END_DIALOG_MODE_ADMINKB = {
    'btns_count': 1,
    'keyboard_view': 'column',
    'buttons_data': [
        {'name': 'Сохранить диалог', 'callback': 'save_private_dialog'},
    ]
}
