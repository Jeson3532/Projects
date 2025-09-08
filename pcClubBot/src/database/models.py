from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from typing import Annotated
from pydantic import Field
from src.utils.config.database import DBConfig

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


config = DBConfig()

host = config.host
port = config.port
user = config.user
password = config.password
dbname = config.dbname
url = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{dbname}"

engine = create_async_engine(url)
session_maker = async_sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    ...
class DBUsers(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, comment="Телеграмм айди.")
    name: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column()
    email: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column()
    rank: Mapped[str] = mapped_column()
    balance: Mapped[float] = mapped_column()
    num_parishes: Mapped[int] = mapped_column(comment="Количество приходов в заведение.", default=0)
    authorized: Mapped[bool] = mapped_column(default=False)

    @classmethod
    async def create_table(cls):
        async with engine.begin() as connect:
            logger.info("Создаю базу данных...")
            query = cls.metadata.create_all
            await connect.run_sync(query)
            logger.info("База данных создана!")






