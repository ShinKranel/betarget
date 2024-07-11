import pytest
from httpx import AsyncClient

from conftest import test_urls
from src.logger import test_logger
from src.vacancy.service import delete_vacancy_without_checking


@pytest.mark.asyncio
async def test_create_vacancy_successfully(auth_async_client: AsyncClient, vacancy_data: dict):
    response = await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    created_data = response.json()
    assert response.status_code == 201 and created_data.get("job_title") == "string"
    await delete_vacancy_without_checking(created_data.get("id"))


@pytest.mark.asyncio
async def test_create_vacancy_unauthorized(async_client: AsyncClient, vacancy_data: dict):
    response = await async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_create_vacancy_incorrect(auth_async_client: AsyncClient, vacancy_data: dict):
    response = await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_all_vacancies(auth_async_client: AsyncClient, vacancy_data: dict):
    for _ in range(5):
        await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    response = await auth_async_client.get(test_urls["vacancy"].get("get_all_vacancies"))
    all_data = response.json()
    assert response.status_code == 200 and all([vac.get("id") and vac.get("city") == "string" for vac in all_data]) and len(all_data) == 5
    for vac in all_data:
        await delete_vacancy_without_checking(vac.get("id"))

    
@pytest.mark.asyncio
async def test_get_all_vacancies_empty(auth_async_client: AsyncClient):
    response = await auth_async_client.get(test_urls["vacancy"].get("get_all_vacancies"))
    assert response.status_code == 200 and len(response.json()) == 0


@pytest.mark.asyncio
async def test_update_vacancy_successfully(auth_async_client: AsyncClient, vacancy_data: dict):
    create_response = await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    vacancy_data = create_response.json()
    new_data = vacancy_data.copy()
    new_data["job_title"] = "new string"
    response = await auth_async_client.put(test_urls["vacancy"].get("update_user_vacancy"), json=new_data)
    updated_data = response.json()
    assert response.status_code == 200 and updated_data.get("job_title") == "new string" and updated_data.get("city") == vacancy_data.get("city")
    await delete_vacancy_without_checking(vacancy_data.get("id"))


@pytest.mark.asyncio
async def test_update_vacancy_unauthorized(async_client: AsyncClient, vacancy_data: dict):
    response = await async_client.put(test_urls["vacancy"].get("update_user_vacancy"), json=vacancy_data)
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_update_vacancy_incorrect(auth_async_client: AsyncClient, vacancy_data: dict):
    response = await auth_async_client.put(test_urls["vacancy"].get("update_user_vacancy"), json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_user_vacancy(auth_async_client: AsyncClient, vacancy_data: dict):
    create_response = await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    created_data = create_response.json()
    response = await auth_async_client.get(test_urls["vacancy"].get("get_user_vacancy") + f"{created_data.get("id")}")
    assert response.status_code == 200 and response.json().get("id") == created_data.get("id")
    await delete_vacancy_without_checking(created_data.get("id"))


@pytest.mark.asyncio
async def test_get_user_vacancy_unauthorized(async_client: AsyncClient, vacancy_data: dict):
    response = await async_client.get(test_urls["vacancy"].get("get_user_vacancy") + "1")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_delete_vacancy_successfully(auth_async_client: AsyncClient, vacancy_data: dict):
    create_response = await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    created_data = create_response.json()
    response = await auth_async_client.delete(test_urls["vacancy"].get("delete_user_vacancy") + f"{created_data.get('id')}")
    assert response.status_code == 200
