from aiogram.fsm.state import State, StatesGroup


class AnketaStates(StatesGroup):
    started = State()
    finished = State()


class AdminStates(StatesGroup):
    ...


class ConnectToAdmin(StatesGroup):
    started = State()
