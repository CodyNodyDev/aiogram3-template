from dataclasses import dataclass
from typing import Optional

from aiogram.fsm.storage.base import BaseStorage


@dataclass
class Settings:

    """Settings for telegram bot"""

    bot_token: str
    storage: Optional[BaseStorage]
    drop_pending_updates: bool
    parse_mode: any
    admins_chat_id: list

    # postgres_host: str
    # postgres_db: str
    # postgres_user: str
    # postgres_password: str
    # postgres_port: str
    # postgres_data: str
    #
    # redis_host: str
    # redis_port: int
    # redis_database: int
