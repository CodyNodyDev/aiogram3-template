from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum
from typing import Any, Optional
from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

# from database.base import Database
# from utils.config import DB_NAME, DB_PASSWORD, DB_USER, DB_HOST, DB_PORT

Base = declarative_base()


class User(Base):
    """
    Model for connect to postgres
    """

    __tablename__ = "users"

    userid = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    reg_date = Column(String)
    feedback = Column(String)

    def __repr__(self):
        return "<User(userid={}, username='{}', firstname='{}', lastname='{}', reg_date='{}', feedback='{}')>"\
                .format(self.userid, self.username, self.firstname, self.lastname, self.reg_date, self.feedback)


class Project(Base):
    """
    Model for connect to postgres
    """

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    preview_text = Column(String)
    description = Column(String)
    link = Column(String)
    path_to_img = Column(String)

    def __repr__(self):
        return "<Project(id={}, name='{}', preview_text='{}', description='{}', link='{}', path_to_img='{}')>"\
                .format(self.id, self.name, self.preview_text, self.description, self.link, self.path_to_img)


class UserParams(Enum):
    """
    Model for python script
    """

    TABLE_NAME: str = "users"

    USER_ID_COL: str = 'userid'
    USER_NAME_COL: str = 'username'
    USER_FIRST_NAME_COL: str = 'firstname'
    USER_LAST_NAME_COL: str = 'lastname'
    USER_REG_DATE_COL: str = 'reg_date'
    FEEDBACK_COL: str = 'feedback'


class ProjectParams(Enum):
    """
    Model for python script
    """

    TABLE_NAME: str = "projects"

    ID_COL: str = 'id'

    NAME_COL: str = 'name'
    PREVIEW_COL: str = 'preview_text'
    DESCRIPTION_COL: str = 'description'
    LINK_COL: str = 'link'
    PATH_TO_IMG_COL: str = 'path_to_img'


class Database(ABC):
    """
    Simple Database API
    """

    @abstractmethod
    async def create_tables(self) -> None:
        """
        Create tables in database.
        """

        pass

    @abstractmethod
    async def add_user(self, user_id: int, user_data: User) -> None:
        """
        Add a new user to the database.

        Args:
            user_data (User): User object of user to add.
            user_id (user id): The ID of user to add.
        """

        pass

    @abstractmethod
    async def get_user_parameter(self, user_id: int, parameter: str) -> Any:
        """
        Get a specific parameter of a user.

        Args:
            user_id (int): The ID of the user.
            parameter (str): The name of the parameter.

        Returns:
            Any: The value of the parameter.
        """

        pass

    @abstractmethod
    async def update_user_parameter(self, user_id: int, parameter: str, value: Any) -> None:
        """
        Update a specific parameter of a user.

        Args:
            user_id (int): The ID of the user.
            parameter (str): The name of the parameter.
            value (Any): The new value of the parameter.
        """

        pass

    @abstractmethod
    async def get_project_parameter(self, param_name: str) -> Optional[str]:
        """
        Get a specific settings parameter.

        Args:
            param_name (str): The name of the parameter.

        Returns:
            Optional[str]: The value of the parameter, or None if it doesn't exist.
        """

        pass

    @abstractmethod
    async def update_project_parameter(self, param_name: str, value: str) -> None:
        """
        Update a specific settings parameter.

        Args:
            param_name (str): The name of the parameter.
            value (str): The new value of the parameter.
        """

        pass



