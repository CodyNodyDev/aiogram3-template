from aiogram import Router

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.filters import StateFilter


""" Router administrator's commands """

router = Router()


# TODO: добавить фальтр админа
@router.message(Command('admin'), StateFilter(None))
async def main_menu_handler(message: Message):
    """
    This handler receives messages for admins
    """

    await message.answer('Hello admin')
