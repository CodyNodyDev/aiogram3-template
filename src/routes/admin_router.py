import traceback
from typing import Any, Dict

from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from filters.AdminFilter import AdminFilter
from utils import SendExceptionService

""" Router administrator's commands """

router = Router()


@router.message(Command('admin'), StateFilter(None), AdminFilter())
async def main_menu_handler(message: Message, data: Dict[str, Any]) -> None:
    """
    This handler receives messages for admins

    :param message:
    :param data:
    """

    try:
        await message.answer('Hello admin')

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())
