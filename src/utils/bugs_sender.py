from datetime import datetime
from aiogram import Bot

from utils.config import CHANNEL_ID


class SendExceptionService:
    def __init__(self, bot: Bot):
        self._bot: Bot = bot

    async def send_ex(self, value: str = None, traceback: str = None):
        bot_info = await self._bot.me()
        ex_message = f"""
Bot_name: 
{bot_info.username}        

Error time: 
{datetime.now()}

Error Value:
{value}

Traceback:
{traceback}
        """
        text_parts = self.split_text(ex_message)
        for text_part in text_parts:
            await self._bot.send_message(chat_id=CHANNEL_ID, text=text_part)

    @staticmethod
    def split_text(resp_text: str, max_length: int = 4000) -> list:
        """
          Split text into parts of max_length.
        """

        parts = []
        while len(resp_text) > 0:
            part = resp_text[:max_length]
            parts.append(part)
            resp_text = resp_text[max_length:]
        return parts
