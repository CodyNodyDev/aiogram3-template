from aiogram import Bot, Dispatcher

from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from settings import Settings
from utils.loggers import setup
from utils.bugs_channel import SendExceptionService
from utils.config import TOKEN, DROP_PENDING_UPDATES, REDIS_URL
from runners import run_polling

from src.factories import create_dispatcher, create_bot


def main() -> None:
    setup()

    settings: Settings = Settings(
                            bot_token=TOKEN,
                            storage=RedisStorage.from_url(url=REDIS_URL),
                            drop_pending_updates=DROP_PENDING_UPDATES,
                            parse_mode=ParseMode.HTML,
    )
    bot: Bot = create_bot(settings=settings)
    exception_service = SendExceptionService(bot)
    dispatcher: Dispatcher = create_dispatcher(
                                        settings=settings,
                                        exception_service=exception_service
    )

    return run_polling(
                    dispatcher=dispatcher,
                    bot=bot
    )


if __name__ == "__main__":
    main()
