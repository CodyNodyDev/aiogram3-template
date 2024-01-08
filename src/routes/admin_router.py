from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from filters.AdminFilter import AdminFilter

""" Router administrator's commands """

router = Router()


@router.message(Command('admin'), StateFilter(None), AdminFilter())
async def main_menu_handler(message: Message) -> None:
    """
    This handler receives messages for admins

    :param message:
    """

    await message.answer('Hello admin')
