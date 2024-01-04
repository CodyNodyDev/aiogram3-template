from typing import Any

from aiogram import Bot, Dispatcher

from aiogram.client.session.aiohttp import AiohttpSession

from settings import Settings
from routes import get_handlers_router


def create_dispatcher(settings: Settings, exception_service: Any) -> Dispatcher:
    """
    :return: Configured Dispatcher with
            included routers
    """

    dispatcher: Dispatcher = Dispatcher(
        name="main_dispatcher",
        settings=settings,
        storage=settings.storage,
        exception_service=exception_service
    )

    dispatcher.include_router(
        get_handlers_router()
    )

    return dispatcher


def create_bot(settings: Settings) -> Bot:
    """
    :return: Configured Bot
    """

    session: AiohttpSession = AiohttpSession()
    return Bot(
        token=settings.bot_token,
        parse_mode=settings.parse_mode,
        session=session,
    )
