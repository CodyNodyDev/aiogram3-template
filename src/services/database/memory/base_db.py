from abc import ABC, abstractmethod
from typing import Union, List


class MemoryDatabase(ABC):

    @abstractmethod
    async def push(self, key: str, value: Union[bytes, memoryview, str, int, float]) -> None:
        """Push a value to the list stored at the given key."""
        pass

    @abstractmethod
    async def pop(self, key: str) -> str | list | None:
        """Remove and get the first element in the list stored at the given key."""
        pass

    @abstractmethod
    async def get(self, key: str) -> str:
        """Get the value from the given key."""
        pass

    @abstractmethod
    async def range(self, key: str, start: int, end: int) -> List[str]:
        """Get a range of elements from the list stored at the given key."""
        pass

    @abstractmethod
    async def left_push(self, key: str, value: Union[bytes, memoryview, str, int, float]) -> None:
        """
        Push the value at the start of the list stored at key.

        :param key: The key of the list.
        :param value: The value to be pushed.
        """

    @abstractmethod
    async def delete(self, key: str) -> None:
        """Delete the given key."""
        pass
