from src.logger import test_logger as logger
from httpx import AsyncClient


async def get_auth_token(async_client: AsyncClient) -> dict[str, str]:
    response = await async_client.post("/register", json={
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
    
    logger.debug(f"Register response status code: {response.status_code}")
    logger.debug(f"Register response headers: {response.headers}")
    logger.debug(f"Register response content: {response.content}")

    if response.status_code not in [201, 400]:
        raise ValueError("User registration failed")

    login_data = {
        "username": "auth@example.com",
        "password": "AuthTest172"
    }
    r = await async_client.post("/login", data=login_data)

    logger.debug(f"Login response status code: {r.status_code}")
    logger.debug(f"Login response headers: {r.headers}")
    logger.debug(f"Login response content: {r.content}")

    token = r.headers.get('set-cookie')
    if not token:
        logger.error("Login failed, no 'set-cookie' header in response")
        raise ValueError("Login failed, no 'set-cookie' header in response")

    return {"bonds": token.split(";")[0][6:]}
