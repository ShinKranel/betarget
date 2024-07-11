import pytest
from httpx import AsyncClient

from conftest import test_urls
from src.logger import test_logger as logger
# from src.user.service import get_user_by_username, update_user, update_user_profile_picture, delete_user


@pytest.mark.asyncio
async def test_update_user(auth_async_client: AsyncClient, user_data: dict):
    init_user_data = user_data.copy()
    new_data = init_user_data.copy()
    del new_data["profile_picture"]
    new_data["phone_number"] = "+79998887766"
    new_data["github"] = "https://github.com/"
    logger.info(f"User data {user_data}")
    response = await auth_async_client.put(url=test_urls["user"].get("update"), json=new_data)
    response_data = response.json()
    logger.info(f"Response data {response_data}")
    response_phone = response_data.get("phone_number")
    response_github = response_data.get("github")
    assert response.status_code in [200, 204] and response_phone == "tel:+7-999-888-77-66" and response_github == "https://github.com/"
