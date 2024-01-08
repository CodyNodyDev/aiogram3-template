from aiogram.fsm.state import State, StatesGroup


class ConnectToAdmin(StatesGroup):
    """
    Start to communication user with admin
    """

    started = State()
