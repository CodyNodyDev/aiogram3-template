from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message, InlineQuery
from utils.config import ADMINS_ID


class AdminFilter(BaseFilter):
    """
    Filter to check if the user is an admin.
    """

    async def __call__(self, message: Union[Message, InlineQuery]) -> bool:
        """
        Check if the user is an admin based on their chat id.

        Args:
            message (Union[Message, InlineQuery]):
            The message or inline query from the user.

        Returns:
            bool: True if the user is an admin, False otherwise.
        """

        try:
            user_id = message.chat.id
        except AttributeError:
            try:
                user_id = message.message.chat.id
            except AttributeError as e:
                raise AttributeError("Unable to extract chat id from message") from e

        return user_id in ADMINS_ID
