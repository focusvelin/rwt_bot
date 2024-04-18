from database.models import User, Task, async_session
from sqlalchemy import select, insert
from sqlalchemy.sql import text
from asyncio import run

async def get_user(user_id: int):
    async with async_session() as session:
        stmt = select(User).where(User.tg_id == user_id)
        result = await session.scalar(stmt)
        return result

async def create_user(user_id: int, username: str):
    async with async_session() as session:
        stmt = insert(User).values(name=username,tg_id=user_id)
        await session.execute(stmt)
        await session.commit()

async def create_task(descr, begin_time, end_time, user_id):
    async with async_session() as session:
        stmt = insert(Task).values(descr=descr, begin_time=begin_time, end_time=end_time, user_id=user_id)
        await session.execute(stmt)
        await session.commit()

async def get_task_list(user_id: int, date: str):
    async with async_session() as session:
        stmt = select(Task).where(text(f"begin_time::varchar LIKE '{date}_%' and user_id={user_id}"))
        result = await session.scalars(stmt)
        return result

async def get_task_dates(user_id: int):
    async with async_session() as session:
        stmt = text(f"SELECT DISTINCT TO_CHAR(begin_time, 'YYYY-MM-DD') FROM tasks WHERE user_id={user_id}")
        result = await session.scalars(stmt)
        return result

    

