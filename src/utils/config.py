from typing import Final

from decouple import config


"""
The typing module's Final() annotation type is a construct that indicates 
to type controllers that a variable with a given name cannot be reassigned 
a value or that the variable is overridden in a subclass.

Install the welcome handler and the main menu handler
"""


TOKEN: Final[str] = config('TOKEN', default='')
ADMINS_ID: Final[list] = config('ADMINS_ID', default='')
REDIS_URL: Final[str] = config('REDIS_URL', default='')

DROP_PENDING_UPDATES = True

# DB_PORT: Final[str] = config('', default='')
# DB_HOST: Final[str] = config('', default='')
# DB_NAME: Final[str] = config('', default='')
# DB_USER: Final[str] = config('', default='')
# DB_PASSWORD: Final[str] = config('', default='')

