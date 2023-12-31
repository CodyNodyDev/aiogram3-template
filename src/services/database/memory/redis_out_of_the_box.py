from typing import Union

from redis.asyncio.client import Redis

from src.services.database.memory.base_db import MemoryDatabase
from src.utils.config import REDIS_URL


"""
Doc:
https://docs.aiogram.dev/en/dev-3.x/dispatcher/finite_state_machine/storages.html
"""


class RedisDB(MemoryDatabase):
    """
    Class for managing Redis operations.
    """

    def __init__(self):
        """
        Initialize the RedisDB with given host, port and db.
        """

        self._redis_db = Redis.from_url(url=REDIS_URL)

    async def push(self, key: str, value: Union[bytes, memoryview, str, int, float]):
        """
        Push the value at the end of the list stored at key.

        :param key: The key of the list.
        :param value: The value to be pushed.
        """

        await self._redis_db.rpush(key, value)

    async def pop(self, key: str) -> None:
        """
        Remove and get the first element in the list stored at key.

        :param key: The key of the list.
        """

        await self._redis_db.lpop(key)

    async def get(self, key: str) -> str:
        """
        Get value from key

        :param key: The key of value.
        """

        return await self._redis_db.get(key)

    async def range(self, key: str, start: int, end: int) -> list:
        """
        Get a range of elements from the list stored at key.

        :param key: The key of the list.
        :param start: The start index of the range.
        :param end: The end index of the range.
        """

        return [item.decode() for item in await self._redis_db.lrange(key, start, end)]

    async def delete(self, key: str) -> None:
        """
        Delete the key.

        :param key: The key to be deleted.
        """

        await self._redis_db.delete(key)

    async def left_push(self, key: str, value: Union[bytes, memoryview, str, int, float]) -> None:
        """
        Push the value at the start of the list stored at key.

        :param key: The key of the list.
        :param value: The value to be pushed.
        """

        await self._redis_db.lpush(key, value)

