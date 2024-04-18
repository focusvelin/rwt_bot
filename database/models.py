from sqlalchemy import BigInteger, String, TIMESTAMP, ForeignKey
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from typing import List

from config.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS

engine = create_async_engine(f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)

async_session = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    tg_id = mapped_column(BigInteger, unique=True)

class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    descr: Mapped[str] = mapped_column(String(100))
    begin_time = mapped_column(TIMESTAMP)
    end_time = mapped_column(TIMESTAMP)
    user_id = mapped_column(ForeignKey("users.tg_id"))


