from backend.src.config import settings
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from backend.src.auth.base_config import auth_backend, fastapi_users
from backend.src.auth.schemas import UserRead, UserCreate

from backend.src.auth.router import router as router_user
from backend.src.resume.router import router as router_resume
from backend.src.vacancy.router import router as router_vacancy
from backend.src.pages.router import router as router_pages

app = FastAPI()

middleware_settings = settings.middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=middleware_settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

app.mount(
    "/static",
    StaticFiles(directory='frontend/src/static'),
    name="static",
)


auth_prefix = '/api/v1/auth'
app.include_router(router_user, prefix=auth_prefix, tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(), prefix=auth_prefix, tags=["auth"])
app.include_router(fastapi_users.get_auth_router(auth_backend), tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), tags=["auth"])

app.include_router(router_vacancy, prefix="/api/v1/vacancy", tags=["vacancy"])
app.include_router(router_resume, prefix="/api/v1/resume", tags=["resume"])
app.include_router(router_pages, tags=["pages"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
