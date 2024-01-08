from typing import Final

import os
from dotenv import load_dotenv


"""
The typing module's Final() annotation type is a construct that indicates 
to type controllers that a variable with a given name cannot be reassigned 
a value or that the variable is overridden in a subclass.

Install the welcome handler and the main menu handler
"""

load_dotenv()

TOKEN: Final[str] = os.getenv('TOKEN', default='')
ADMINS_ID: Final[list] = str(os.getenv('ADMINS_ID', default='')).split()
REDIS_URL = os.getenv('REDIS_URL', default='')

DB_PORT: Final[int] = int(os.getenv("DB_PORT"))
DB_HOST: Final[str] = os.getenv("DB_HOST")
DB_NAME: Final[str] = os.getenv("DB_NAME")
DB_USER: Final[str] = os.getenv("DB_USER")
DB_PASSWORD: Final[str] = os.getenv("DB_PASSWORD")

CHANNEL_ID = -1002032079838

DROP_PENDING_UPDATES = True

THROTTLING_TIME_PERIOD: Final[int] = 5
THROTTLING_MAX_RATE: Final[int] = 5

# LOCAL URLS
DIALOGS_URL = 'assets/dialogs/'
