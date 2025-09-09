from src.database.models import DBUsers
from src.database.models import session_maker, engine, DBUsers

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select, exists, insert
from fastapi import HTTPException
class BaseMethods:
    @classmethod
    async def check_auth_user(cls, id_: int):
        async with session_maker() as session:
            query = select(exists().where(DBUsers.id == id_).where(DBUsers.authorized))
            result = await session.execute(query)
            return result.scalar()

    @classmethod
    async def add_user(cls, personal_info: dict):
        async with session_maker() as session:
            new_user = DBUsers(**personal_info)
            session.add(new_user)
            await session.commit()
            return new_user
    @classmethod
    async def get_all(cls):
        async with session_maker() as session:
            query = select(DBUsers)
            result = await session.execute(query)
            return result.scalars().all()







