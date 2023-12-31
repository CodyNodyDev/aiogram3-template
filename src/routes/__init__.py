from aiogram import Router


"""
The typing module's Final() annotation type is a construct that indicates 
to type controllers that a variable with a given name cannot be reassigned 
a value or that the variable is overridden in a subclass.

Install the welcome handler and the main menu handler
"""


def get_handlers_router() -> Router:
    from . import (
        admin_router,
        common_router,
        user_router,
    )

    router = Router()

    # Здесь добавляем миддлвари в роутер на сообщения и коллбеки

    router.include_routers(
        admin_router.router,
        common_router.router,
        user_router.router,
    )

    return router
