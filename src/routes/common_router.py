import traceback
from typing import Any, Dict

from aiogram import Router

from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.types import Message

from keyboards.inline.constructor import KBuilder
from utils.constants import MSG, MAIN_KB
from utils import SendExceptionService

""" Router for /start, /help, /info /new_name commands """

router = Router()


@router.message(CommandStart(), StateFilter(None))
async def start_handler(message: Message, data: Dict[str, Any]) -> None:
    """
    This handler receives messages with `/start` command

    :param message: Answer to user
    :param data:
    """

    try:
        await message.answer(MSG['HELLO'].format(
            message.from_user.full_name,
            message.from_user.id,
            ),
            reply_markup=await KBuilder(MAIN_KB).build_keyboard()
        )

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())


@router.message(Command('new_name'), StateFilter(None))
async def new_name_handler(message: Message, data: Dict[str, Any]) -> None:
    """
    Set bot's name for current chat

    :param message: Reply to user message
    :param data:
    """

    try:
        # TODO: Здесь должно быть изменение контекста для пользователя -> меняем имя бота

        await message.reply(
            text='Тут должен включаться стейт и бот должен запоминать написанное имя',
        )

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())
