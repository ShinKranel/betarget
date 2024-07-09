import asyncio
from typing import AsyncGenerator
import asyncpg
import pytest
from httpx import AsyncClient
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.base import Base
from src.config import settings
from src.db import get_async_session
from src.main import app
from utils import get_auth_token

test_db_settings = settings.test_database


async def create_test_database():
    conn = await asyncpg.connect(
        user=test_db_settings.DB_TEST_USER,
        password=test_db_settings.DB_TEST_PASS,
        database="postgres",
        host=test_db_settings.DB_TEST_HOST,
        port=test_db_settings.DB_TEST_PORT,
    )
    await conn.execute(f"CREATE DATABASE {test_db_settings.DB_TEST_NAME}")
    await conn.close()


async def drop_test_database():
    conn = await asyncpg.connect(
        user=test_db_settings.DB_TEST_USER,
        password=test_db_settings.DB_TEST_PASS,
        database="postgres",
        host=test_db_settings.DB_TEST_HOST,
        port=test_db_settings.DB_TEST_PORT,
    )
    await conn.execute(f"DROP DATABASE IF EXISTS {test_db_settings.DB_TEST_NAME}")
    await conn.close()


async def setup_test_database():
    try:
        await create_test_database()
    except asyncpg.exceptions.DuplicateDatabaseError:
        await drop_test_database()
        await create_test_database()

    engine_test = create_async_engine(
        test_db_settings.DATABASE_URL_ASYNC, poolclass=NullPool
    )
    async_session_maker = async_sessionmaker(engine_test, expire_on_commit=False)
    Base.metadata.bind = engine_test

    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    return engine_test, async_session_maker


async def teardown_test_database(engine_test):
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await drop_test_database()


@pytest.fixture(scope="session")
async def db():
    engine_test, async_session_maker = await setup_test_database()

    yield async_session_maker

    await teardown_test_database(engine_test)


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with get_async_session() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session


async def auth_token(client: AsyncClient) -> dict[str, str]:
    return await get_auth_token(client)


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="module")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://localhost:9999") as client:
        yield client


@pytest.fixture(scope="module")
async def auth_async_client(async_client: AsyncClient) -> AsyncClient:
    token = await auth_token(async_client)
    async_client.cookies.update(token)
    return async_client
