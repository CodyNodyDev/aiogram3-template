from typing import Optional, Any

from services.database.models import User, Project, Database
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from utils.config import DB_NAME, DB_PASSWORD, DB_USER, DB_HOST, DB_PORT

Base = declarative_base()


class Postgres(Database):
    """
    Doc in models.py
    """

    def __init__(self):
        self._DB_HOST = DB_HOST
        self._DB_PORT = DB_PORT
        self._DB_NAME = DB_NAME
        self._DB_USER = DB_USER
        self._DB_PASSWORD = DB_PASSWORD

        try:
            self.engine = create_async_engine(
                f"postgresql+asyncpg://{self._DB_USER}:{self._DB_PASSWORD}@{self._DB_HOST}:{self._DB_PORT}/{self._DB_NAME}"
            )
            self.Session = async_sessionmaker(bind=self.engine, expire_on_commit=False, class_=AsyncSession)

        except Exception as e:
            print('class <Postgres> connection error:', e)

    async def create_tables(self) -> None:
        pass

    async def add_user(self, user_id: int, user_data: User) -> None:
        try:
            async with self.Session() as session:
                if await session.get(User, user_id):
                    return None
                session.add(user_data)
                await session.commit()

        except Exception as e:
            print('class <Postgres> add_user error:', e)

    async def get_user_parameter(self, user_id: int, parameter: str) -> Any:
        try:
            async with self.Session() as session:
                user = await session.get(User, user_id)
                return getattr(user, parameter, None)

        except Exception as e:
            print('class <Postgres> get_user_parameter error:', e)

    async def update_user_parameter(self, user_id: int, parameter: str, value) -> None:
        try:
            async with self.Session() as session:
                user = await session.get(User, user_id)
                if user:
                    setattr(user, parameter, value)
                    await session.commit()

        except Exception as e:
            print('class <Postgres> update_user_parameter error:', e)

    async def get_project_parameter(self, param_name: str) -> Optional[str]:
        try:
            async with self.Session() as session:
                setting = await session.get(Project, param_name)
                return setting.value if setting else None

        except Exception as e:
            print('class <Postgres> get_project_parameter error:', e)

    async def update_project_parameter(self, param_name: str, value: str) -> None:
        try:
            async with self.Session() as session:
                setting = await session.get(Project, param_name)
                if setting:
                    setting.value = value
                    await session.commit()

        except Exception as e:
            print('class <Postgres> update_project_parameter error:', e)
