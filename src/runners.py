from aiogram import Bot, Dispatcher

from settings import Settings


async def polling_startup(bot, settings: Settings) -> None:
    await bot.delete_webhook(drop_pending_updates=settings.drop_pending_updates)

    if settings.drop_pending_updates:
        print('Webhooks deleted...')


def run_polling(
        dispatcher: Dispatcher,
        bot: Bot,
) -> None:

    """
    Bot start polling
    """

    dispatcher.startup.register(polling_startup)
    return dispatcher.run_polling(bot)
