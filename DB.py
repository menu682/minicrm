from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlmodel import SQLModel

DATABASE_URL = "sqlite+aiosqlite:///./database.db"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(engine, class_ = AsyncSession, expire_on_commit = False)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Підключення до бази даних...")
    async with engine.connect() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    yield

    print("Закриття підключення до бази даних...")
    await engine.dispose()


async def get_database():
    async with SessionLocal() as session:
        yield session