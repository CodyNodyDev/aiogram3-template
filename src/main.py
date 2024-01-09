from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from factories import create_dispatcher, create_bot
from runners import run_polling
from services.database.crud import Postgres
from settings import Settings, setup_logs
from utils import SendExceptionService
from utils.config import TOKEN, DROP_PENDING_UPDATES, REDIS_URL


def main() -> None:
    setup_logs()

    settings: Settings = Settings(
                            bot_token=TOKEN,
                            storage=RedisStorage.from_url(url=REDIS_URL),
                            drop_pending_updates=DROP_PENDING_UPDATES,
                            parse_mode=ParseMode.HTML,
                            database=Postgres()
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

# TODO: добавить обработку исключений везде
# TODO: обработку исключений везде вынести на отправку в канал
