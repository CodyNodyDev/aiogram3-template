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
