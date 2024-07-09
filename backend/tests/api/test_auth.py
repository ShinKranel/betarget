# from fastapi.testclient import TestClient


# # REGISTER -----
# def test_register(client: TestClient):
#     response = client.post("/register", json={
#         "email": "test@example.com",
#         "password": "test",
#         "is_active": True,
#         "is_superuser": False,
#         "is_verified": False,
#         "username": "test"
#     })

#     assert response.status_code == 201, "Must be 201 status code"


# def test_register_incorrect(client: TestClient):
#     response = client.post("/register", json={})

#     assert response.status_code == 422, "Must be 422 UNPROCESSABLE_ENTITY status code"


# def test_register_user_already_exist(client: TestClient):
#     response = client.post("/register", json={
#         "email": "test@example.com",
#         "password": "test",
#         "is_active": True,
#         "is_superuser": False,
#         "is_verified": False,
#         "username": "test"
#     })

#     content = response.json()
#     assert content["detail"] == 'REGISTER_USER_ALREADY_EXISTS', "Must be error REGISTER_USER_ALREADY_EXISTS"


# # LOGIN -----
# def test_login(client: TestClient):
#     form_data = {
#         "username": "test@example.com",
#         "password": "test"
#     }
#     response = client.post(
#         "/login",
#         data=form_data,
#         headers={"Content-Type": "application/x-www-form-urlencoded"})

#     assert response.status_code == 204, "Must be 204 status code"


# def test_login_incorrect(client: TestClient):
#     form_data = {
#         "username": "tet@example.com",
#         "password": "test"
#     }
#     response = client.post(
#         "/login",
#         data=form_data,
#         headers={"Content-Type": "application/x-www-form-urlencoded"})

#     assert response.status_code == 400, "Must be 400 BAD_REQUEST status code"
