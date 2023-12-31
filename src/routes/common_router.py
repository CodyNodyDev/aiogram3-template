from aiogram import Router

from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.types import Message

from src.keyboards.inline.constructor import KBuilder
from src.utils.constants import MSG, MAIN_KB

""" Router for /start, /help, /info /new_name commands """

router = Router()


@router.message(CommandStart(), StateFilter(None))
async def start_handler(message: Message):
    """
    This handler receives messages with `/start` command
    """

    await message.answer(MSG['HELLO'].format(
        message.from_user.full_name,
        message.from_user.id,
        ),
        reply_markup=await KBuilder(MAIN_KB).build_keyboard()
    )


@router.message(Command('new_name'), StateFilter(None))
async def start_handler(message: Message):
    """
    Здесь должно быть изменение контекста для пользователя -> меняем имя бота
    """

    await message.reply(
        text='Тут должен включаться стейт и бот должен запоминать написанное имя',
    )
