import asyncio
import logging
import sys
from dataclasses import dataclass

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from src.utils.config import TOKEN
from aiogram.fsm.storage.redis import RedisStorage
from src.states import AnketaStates


REDIS_URL = 'redis://default:mfLDaedN5HAjCofBMFaIBcolD2LDk524@viaduct.proxy.rlwy.net:27015'
dp = Dispatcher(storage=RedisStorage.from_url(REDIS_URL))


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(AnketaStates.started)
    await state.set_data(data={"state": 'started'})
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")



@dp.message()
async def echo_handler(message: types.Message, state: FSMContext) -> None:
    try:
        a = await state.get_data()
        await message.answer(f'your data: {a}')
        b = await state.get_state()
        print(b)
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())















