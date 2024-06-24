from fastapi.testclient import TestClient


# CREATE VACANCY -----
def test_create_vacancy(auth_client: TestClient):
    response = auth_client.post("/vacancy", json={
        "job_title": "string",
        "city": "string",
        "company": "string",
        "experience": "no experience",
        "work_format": "in office",
        "salary": 0,
        "education": "incomplete_secondary",
        "employment_type": "full_time",
        "skills": "string",
        "description": "string"
    })

    assert response.status_code == 201, "Must be 201 CREATED status code"


def test_create_vacancy_unauthorized(client: TestClient):
    response = client.post("/vacancy", json={
        "job_title": "string",
        "city": "string",
        "company": "string",
        "experience": "no experience",
        "work_format": "in office",
        "salary": 0,
        "education": "incomplete_secondary",
        "employment_type": "full_time",
        "skills": "string",
        "description": "string"
    })

    assert response.status_code == 401, "Must be 401 UNAUTHORIZED status code"


def test_create_vacancy_incorrect(auth_client: TestClient):
    response = auth_client.post("/vacancy", json={})

    assert response.status_code == 422, "Must be 422 UNPROCESSABLE_ENTITY status code"


# READ USER VACANCIES -----
def test_read_user_vacancies(auth_client: TestClient):
    response = auth_client.get("/vacancy")

    assert response.status_code == 200, "Must be 200 OK status code"


def test_read_user_vacancies_unauthorized(client: TestClient):
    response = client.get("/vacancy")

    assert response.status_code == 401, "Must be 401 UNAUTHORIZED status code"


# READ USER VACANCY BY ID -----
def test_read_user_vacancy_by_id(auth_client: TestClient):
    response = auth_client.get("/vacancy", params={"vacancy_id": 1})

    assert response.status_code == 200, "Must be 200 OK status code"


def test_read_user_vacancy_by_id_unauthorized(client: TestClient):
    response = client.get("/vacancy", params={"vacancy_id": 1})

    assert response.status_code == 401, "Must be 401 UNAUTHORIZED status code"


def test_read_user_vacancy_by_id_not_fount(auth_client: TestClient):
    response = auth_client.get("/vacancy/10")

    assert response.status_code == 404, "Must be 404 NOT_FOUND status code"


# TODO: add second user for "not_enough_permission status code" checking
# def test_read_user_vacancy_by_id_not_enough_permissions(auth_client: TestClient):
#     response = auth_client.get("/vacancy/1")
#
#     assert response.status_code == 403, "Must be 403 NOT_ENOUGH_PERMISSIONS status code"
