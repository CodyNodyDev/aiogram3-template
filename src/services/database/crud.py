import asyncio

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.utils.config import DB_NAME, DB_PASSWORD, DB_USER, DB_HOST, DB_PORT
from src.services.database.models import User, Project, Database

Base = declarative_base()


class Postgres(Database):
    def __init__(self):
        self._DB_HOST = DB_HOST
        self._DB_PORT = DB_PORT
        self._DB_NAME = DB_NAME
        self._DB_USER = DB_USER
        self._DB_PASSWORD = DB_PASSWORD
        self.engine = create_async_engine(
            f"postgresql+asyncpg://{self._DB_USER}:{self._DB_PASSWORD}@{self._DB_HOST}:{self._DB_PORT}/{self._DB_NAME}"
        )
        self.Session = async_sessionmaker(bind=self.engine, expire_on_commit=False, class_=AsyncSession)

    async def create_tables(self) -> None:
        pass

    async def add_user(self, user_id: int, user_data: User):
        async with self.Session() as session:
            if await session.get(User, user_id):
                return None
            session.add(user_data)
            await session.commit()

    async def get_user_parameter(self, user_id: int, parameter: str):
        async with self.Session() as session:
            user = await session.get(User, user_id)
            return getattr(user, parameter, None)

    async def update_user_parameter(self, user_id: int, parameter: str, value):
        async with self.Session() as session:
            user = await session.get(User, user_id)
            if user:
                setattr(user, parameter, value)
                await session.commit()

    async def get_project_parameter(self, param_name: str):
        async with self.Session() as session:
            setting = await session.get(Project, param_name)
            return setting.value if setting else None

    async def update_project_parameter(self, param_name: str, value: str):
        async with self.Session() as session:
            setting = await session.get(Project, param_name)
            if setting:
                setting.value = value
                await session.commit()
