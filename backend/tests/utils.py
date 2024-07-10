from src.logger import test_logger as logger
from httpx import AsyncClient


async def get_auth_token(async_client: AsyncClient) -> dict[str, str]:
    _ = await async_client.post("/register", json={
        "email": "auth@example.com",
        "password": "AuthTest172",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "auth",
        "telegram": "https://example.com/",
        "whatsapp": "https://example.com/",
        "linkedin": "https://example.com/",
        "github": "https://example.com/",
        "phone_number": "+77777777777",
        "profile_picture": "https://example.com/"
    })
    login_data = {
        "username": "auth@example.com",
        "password": "AuthTest172"
    }
    r = await async_client.post("/login", data=login_data)
    token = r.headers.get('set-cookie')
    return {"bonds": token.split(";")[0][6:]}
