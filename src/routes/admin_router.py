from aiogram import Router

from aiogram.types import Message
from aiogram.filters import Command, StateFilter

from src.filters.AdminFilter import AdminFilter

""" Router administrator's commands """

router = Router()


@router.message(Command('admin'), StateFilter(None), AdminFilter())
async def main_menu_handler(message: Message):
    """
    This handler receives messages for admins
    """

    await message.answer('Hello admin')
