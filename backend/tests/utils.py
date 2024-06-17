from fastapi import Cookie
from starlette.testclient import TestClient


def get_auth_token(client: TestClient) -> Cookie():
    client.post("/register", json={
        "email": "auth@example.com",
        "password": "auth",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "auth"
    })

    login_data = {
        "username": "auth@example.com",
        "password": "auth"
    }
    r = client.post("/login", data=login_data)

    token = r.headers['set-cookie'].split(";")[0]

    return {"bonds": token[6:]}
