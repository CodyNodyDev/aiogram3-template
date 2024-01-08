import traceback
from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject
from services.database.models import Database, User
from utils import SendExceptionService, get_date_time


class AddUserMiddleware(BaseMiddleware):
    """
    Middleware that adds a user to the database
    """

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:
        try:
            try:
                user_id = event.chat.id
            except AttributeError:
                user_id = event.message.chat.id
            try:
                username = event.chat.username
            except Exception as e:
                username = 'None'
                print('ADD USER ERROR:', e)
            try:
                firstname = str(event.chat.first_name)
            except Exception as e:
                firstname = 'None'
                print('ADD USER ERROR:', e)
            try:
                lastname = str(event.chat.last_name)
            except Exception as e:
                lastname = 'None'
                print('ADD USER ERROR:', e)

            reg_date = await get_date_time()
            print(lastname)

            user_data = User(
                userid=user_id,
                username=username,
                firstname=firstname,
                lastname=lastname,
                reg_date=reg_date,
                feedback='None',
            )

            database: Database = data.get("database")

            await database.add_user(user_id=user_id, user_data=user_data)
            return await handler(event, data)

        except Exception as e:
            exception_service: SendExceptionService = data.get("exception_service")
            await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())
