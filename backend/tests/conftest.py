import asyncio

from typing import AsyncGenerator, Generator
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from src.config import settings
from src.main import app
from utils import get_auth_token


test_urls = {
    "auth": {
        "register": "/register",
        "login": "/login",
        "logout": "/logout",
    }
}


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


async def auth_token(client: AsyncClient) -> dict[str, str]:
    return await get_auth_token(client)


@pytest_asyncio.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url=settings.test.BASE_URL) as client:
        yield client


@pytest_asyncio.fixture
async def auth_async_client(async_client: AsyncClient) -> AsyncClient:
    user_data = {
        "username": "test_user",
        "email": "test@ex.com",
        "password": "SuperUsername1233",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "telegram": "https://example.com/",
        "whatsapp": "https://example.com/",
        "linkedin": "https://example.com/",
        "github": "https://example.com/",
        "phone_number": "+77777777777",
        "profile_picture": "https://example.com/",
    }
    _ = await async_client.post(url=test_urls["auth"].get("register"), json=user_data)
    login_response = await async_client.post(url=test_urls["auth"].get("login"), 
        data={"username": user_data.get("email"), "password": user_data.get("password")}
    )
    async_client.cookies = {"bonds": login_response.headers.get("set-cookie").split(";")[0][6:]}
    return async_client