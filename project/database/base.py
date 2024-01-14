from sqlalchemy.pool import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from project.config import db_url


meta = MetaData()


class Base(AsyncAttrs, DeclarativeBase):
    pass


async_engine = create_async_engine(db_url,
                                   echo=True,
                                   poolclass=AsyncAdaptedQueuePool,
                                   future=True)
async_session = async_sessionmaker(bind=async_engine, class_=AsyncEngine, expire_on_commit=False)


async def init_models():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
