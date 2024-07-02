import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi.testclient import TestClient

from backend.src.base import Base
from backend.src.config import settings
from backend.src.db import get_async_session
from backend.src.main import app
from utils import get_auth_token

test_db_settigns = settings.test_database

engine_test = create_async_engine(test_db_settigns.DATABASE_URL_ASYNC, poolclass=NullPool)
async_session_maker = async_sessionmaker(engine_test, expire_on_commit=False)
Base.metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().get_event_loop()
    yield loop
    loop.close()


# SETUP
@pytest.fixture(scope="module")
def client() -> TestClient:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def auth_client(client: TestClient) -> TestClient:
    with TestClient(app, cookies=auth_token(client)) as c:
        yield c


def auth_token(client: TestClient) -> dict[str, str]:
    return get_auth_token(client)


@pytest.fixture(scope="module")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
