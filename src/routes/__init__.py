from aiogram import Router


def get_handlers_router() -> Router:
    from . import (
        admin_router,
        common_router,
        user_router,
        dialog_mode_handlers,
    )

    router = Router()

    # TODO: Здесь добавить миддлвари

    router.include_routers(
        admin_router.router,
        common_router.router,
        user_router.router,
        dialog_mode_handlers.router,
    )

    return router
