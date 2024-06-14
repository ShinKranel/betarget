# from httpx import AsyncClient
#
#
# async def test_create_vacancy(ac: AsyncClient):
#     response = await ac.post("/vacancy", json={
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
#
#     assert response.status_code == 201, "Must be 201 status code"
