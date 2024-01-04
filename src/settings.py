from dataclasses import dataclass
from typing import Optional
import logging

from aiogram.fsm.storage.base import BaseStorage


@dataclass
class Settings:

    """Settings for telegram bot"""

    bot_token: str
    storage: Optional[BaseStorage]
    drop_pending_updates: bool
    parse_mode: any

    # database: TODO: add postgre


def setup_logs(level=logging.INFO) -> None:
    """
    Setup 2 logger:
        1) logs into file logfile.log
        2) logs in console

    :param level:
    """

    logger = logging.getLogger()
    logger.setLevel(level)

    file_handler = logging.FileHandler('logfile.log')
    file_format = logging.Formatter("%(asctime)s - [%(levelname)s] -  %(name)s - "
                                    "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    file_handler.setFormatter(file_format)

    console_handler = logging.StreamHandler()
    console_format = logging.Formatter("%(asctime)s - [%(levelname)s] -  %(name)s - "
                                       "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    console_handler.setFormatter(console_format)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
