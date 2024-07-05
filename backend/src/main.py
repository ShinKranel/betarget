from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from auth.base_config import auth_backend, fastapi_users
from logger import logger
from auth.schemas import UserRead, UserCreate
from config import settings
from db import engine

from vacancy.admin import VacancyAdmin
from resume.admin import ResumeAdmin
from auth.admin import UserAdmin
from admin.auth_backend import AdminAuth

from auth.router import router as router_user
from resume.router import router as router_resume
from vacancy.router import router as router_vacancy


async def start_up(app: FastAPI):
    logger.debug('App started')
    admin_settings = settings.admin
    admin = Admin(app=app, engine=engine, authentication_backend=AdminAuth(secret_key=admin_settings.SECRET_SESSION))
    admin_views = [UserAdmin, ResumeAdmin, VacancyAdmin]
    [admin.add_view(view) for view in admin_views]


async def shut_down(app: FastAPI):
    logger.debug('Shutting down')


@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_up(app)
    yield
    await shut_down(app)


app = FastAPI(lifespan=lifespan)

middleware_settings = settings.middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=middleware_settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

auth_prefix = '/api/v1/auth'
app.include_router(router_user, prefix=auth_prefix, tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(), prefix=auth_prefix, tags=["auth"])
app.include_router(fastapi_users.get_auth_router(auth_backend), tags=["auth"])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate), tags=["auth"])

app.include_router(router_vacancy, prefix="/api/v1/vacancy", tags=["vacancy"])
app.include_router(router_resume, prefix="/api/v1/resume", tags=["resume"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
