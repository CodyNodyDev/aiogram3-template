from aiogram import Router

from middlewares import ThrottlingMiddleware, AddUserMiddleware


def get_handlers_router() -> Router:
    """
    Assembling all routers into one. The middleware is also installed

    :return: Router object (this will main in Dispatcher)
    """

    from . import (
        admin_router,
        common_router,
        user_router,
        dialog_mode_handlers,
    )

    router = Router()

    router.message.middleware(ThrottlingMiddleware())
    router.callback_query.middleware(ThrottlingMiddleware())

    router.message.middleware(AddUserMiddleware())

    router.include_routers(
        admin_router.router,
        common_router.router,
        user_router.router,
        dialog_mode_handlers.router,
    )

    return router
