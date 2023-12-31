from aiogram import Router


def get_handlers_router() -> Router:
    from . import (
        admin_router,
        common_router,
        user_router,
    )

    router = Router()

    # TODO: Здесь добавbить миддлвари

    router.include_routers(
        admin_router.router,
        common_router.router,
        user_router.router,
    )

    return router
