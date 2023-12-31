from aiogram import Router

from src.middlewares import ThrottlingMiddleware


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

    router.include_routers(
        admin_router.router,
        common_router.router,
        user_router.router,
        dialog_mode_handlers.router,
    )

    return router


# TODO: Добить отработку ошибок:

"""
@router.callback_query(F.data.startswith("backer"))
async def on_backer(call: types.CallbackQuery, exc_ser: SendExceptionServes):
    try:
        keyboard = call.data.split(":")[1]
        await call.message.edit_reply_markup(reply_markup=eval(keyboard))
    except Exception as e:
        await exc_ser.send_ex(value=e.__str__(), traceback=traceback.format_exc())
        await call.answer(settings.ERROR_MESSAGE, parse_mode="HTML")
"""
