import pytest
from httpx import AsyncClient

from conftest import test_urls
from src.logger import test_logger
from src.resume.service import delete_resume_without_check
from src.vacancy.service import delete_vacancy_without_checking


@pytest.mark.asyncio
async def test_create_resume_successfully(auth_async_client: AsyncClient, vacancy_data: dict, resume_data: dict):
    vacancy_response = await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    vacancy_data = vacancy_response.json()
    response = await auth_async_client.post(test_urls["resume"].get("create_user_resume"), params={"vacancy_id": vacancy_data.get("id")}, json=resume_data)
    created_data = response.json()
    assert response.status_code == 201 and created_data.get("job_title") == "string"
    await delete_resume_without_check(created_data.get("id"))
    await delete_vacancy_without_checking(vacancy_data.get("id"))


@pytest.mark.asyncio
async def test_create_resume_unauthorized(async_client: AsyncClient, resume_data: dict):
    response = await async_client.post(test_urls["resume"].get("create_user_resume"), json=resume_data)
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_create_resume_incorrect(auth_async_client: AsyncClient):
    response = await auth_async_client.post(test_urls["resume"].get("create_user_resume"), json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_all_resumes(auth_async_client: AsyncClient, vacancy_data: dict, resume_data: dict):
    vacancy_response = await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    vacancy_data = vacancy_response.json()
    for _ in range(5):
        await auth_async_client.post(test_urls["resume"].get("create_user_resume"), params={"vacancy_id": vacancy_data.get("id")} , json=resume_data)
    response = await auth_async_client.get(test_urls["resume"].get("get_all_resumes"))
    all_data = response.json()
    assert response.status_code == 200 and all([res.get("id") and res.get("job_title") == "string" for res in all_data]) and len(all_data) == 5
    for res in all_data:
        await delete_resume_without_check(res.get("id"))
    await delete_vacancy_without_checking(vacancy_data.get("id"))


@pytest.mark.asyncio
async def test_get_all_resumes_empty(auth_async_client: AsyncClient, vacancy_data: dict):
    response_vacancy = await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    vacancy_data = response_vacancy.json()
    response = await auth_async_client.get(test_urls["resume"].get("get_all_resumes"))
    assert response.status_code == 200 and len(response.json()) == 0
    await delete_vacancy_without_checking(vacancy_data.get("id"))


@pytest.mark.asyncio
async def test_update_resume_successfully(auth_async_client: AsyncClient, vacancy_data: dict, resume_data: dict):
    create_vacancy = await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    vacancy_data = create_vacancy.json()
    create_response = await auth_async_client.post(test_urls["resume"].get("create_user_resume"), params={"vacancy_id": vacancy_data.get("id")}, json=resume_data)
    resume_data = create_response.json()
    new_data = resume_data.copy()
    new_data["job_title"] = "new string"
    response = await auth_async_client.put(test_urls["resume"].get("update_user_resume"), json=new_data)
    updated_data = response.json()
    assert response.status_code == 200 and updated_data.get("job_title") == "new string" and updated_data.get("expected_salary") == resume_data.get("expected_salary")
    await delete_resume_without_check(resume_data.get("id"))
    await delete_vacancy_without_checking(vacancy_data.get("id"))


@pytest.mark.asyncio
async def test_update_resume_unauthorized(async_client: AsyncClient, resume_data: dict):
    response = await async_client.put(test_urls["resume"].get("update_user_resume"), json=resume_data)
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_update_resume_incorrect(auth_async_client: AsyncClient):
    response = await auth_async_client.put(test_urls["resume"].get("update_user_resume"), json={})
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_user_resume(auth_async_client: AsyncClient, vacancy_data: dict, resume_data: dict):
    create_vacancy = await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    vacancy_data = create_vacancy.json()
    create_response = await auth_async_client.post(test_urls["resume"].get("create_user_resume"), params={"vacancy_id": vacancy_data.get("id")}, json=resume_data)
    created_data = create_response.json()
    response = await auth_async_client.get(test_urls["resume"].get("get_user_resume") + f"{created_data.get('id')}")
    assert response.status_code == 200 and response.json().get("id") == created_data.get("id")
    await delete_resume_without_check(created_data.get("id"))
    await delete_vacancy_without_checking(vacancy_data.get("id"))


@pytest.mark.asyncio
async def test_get_user_resume_unauthorized(async_client: AsyncClient, resume_data: dict):
    response = await async_client.get(test_urls["resume"].get("get_user_resume") + "1")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_delete_resume_successfully(auth_async_client: AsyncClient, vacancy_data: dict, resume_data: dict):
    create_vacancy = await auth_async_client.post(test_urls["vacancy"].get("create_user_vacancy"), json=vacancy_data)
    vacancy_data = create_vacancy.json()
    create_response = await auth_async_client.post(test_urls["resume"].get("create_user_resume"), params={"vacancy_id": vacancy_data.get("id")}, json=resume_data)
    created_data = create_response.json()
    response = await auth_async_client.delete(test_urls["resume"].get("delete_user_resume") + f"{created_data.get('id')}")
    assert response.status_code == 200
    await delete_vacancy_without_checking(vacancy_data.get("id"))

