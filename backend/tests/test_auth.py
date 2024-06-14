from httpx import AsyncClient

from backend.tests.conftest import client


def test_register():
    response = client.post("/register", json={
        "email": "test@example.com",
        "password": "test",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "test"
    })

    assert response.status_code == 201, "Must be 201 status code"

