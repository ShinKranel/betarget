import pytest
from httpx import AsyncClient

from src.logger import test_logger

# class VacancyRead(BaseModel):
#     id: int
#     user_id: UUID4
#     job_title: str | None = Field(None, min_length=1, max_length=60)
#     city: str | None = Field(None, max_length=50)
#     company: str = Field(..., min_length=1, max_length=50)
#     experience: Experience | None
#     work_format: WorkFormat | None
#     salary: int | None = Field(None, ge=0)
#     education: Education | None
#     employment_type: EmploymentType | None
#     skills: list[str] | None = Field(None, max_length=20)
#     description: str | None = Field(None, max_length=2000)
#     created_at: datetime
#     expiration_date: datetime


# CREATE VACANCY -----
@pytest.mark.asyncio
async def test_create_successful(auth_async_client: AsyncClient):
    response = await auth_async_client.post("/api/v1/vacancy/", json={
        "job_title": "string",
        "city": "string",
        "company": "string",
        "experience": "no experience",
        "work_format": "in office",
        "salary": 25000,
        "education": "incomplete_secondary",
        "employment_type": "full_time",
        "skills": [
            "string"
        ],
        "description": "string"
    })

    test_logger.info(f"Response: {response.content}")
    assert response.status_code == 201, "Must be 201 CREATED status code"


# def test_create_vacancy_unauthorized(client: TestClient):
#     response = client.post("/vacancy", json={
#         "job_title": "string",
#         "city": "string",
#         "company": "string",
#         "experience": "no experience",
#         "work_format": "in office",
#         "salary": 0,
#         "education": "incomplete_secondary",
#         "employment_type": "full_time",
#         "skills": "string",
#         "description": "string"
#     })

#     assert response.status_code == 401, "Must be 401 UNAUTHORIZED status code"


# def test_create_vacancy_incorrect(auth_client: TestClient):
#     response = auth_client.post("/vacancy", json={})

#     assert response.status_code == 422, "Must be 422 UNPROCESSABLE_ENTITY status code"


# # READ USER VACANCIES -----
# def test_read_user_vacancies(auth_client: TestClient):
#     response = auth_client.get("/vacancy")

#     assert response.status_code == 200, "Must be 200 OK status code"


# def test_read_user_vacancies_unauthorized(client: TestClient):
#     response = client.get("/vacancy")

#     assert response.status_code == 401, "Must be 401 UNAUTHORIZED status code"


# # READ USER VACANCY BY ID -----
# def test_read_user_vacancy_by_id(auth_client: TestClient):
#     response = auth_client.get("/vacancy", params={"vacancy_id": 1})

#     assert response.status_code == 200, "Must be 200 OK status code"


# def test_read_user_vacancy_by_id_unauthorized(client: TestClient):
#     response = client.get("/vacancy", params={"vacancy_id": 1})

#     assert response.status_code == 401, "Must be 401 UNAUTHORIZED status code"


# def test_read_user_vacancy_by_id_not_fount(auth_client: TestClient):
#     response = auth_client.get("/vacancy/10")

#     assert response.status_code == 404, "Must be 404 NOT_FOUND status code"