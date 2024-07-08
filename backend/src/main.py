from contextlib import asynccontextmanager

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
from fastapi_limiter import FastAPILimiter

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from logger import logger
from config import settings
from db import engine
from redis_ import redis_connection
from sse import sse_router

from vacancy.admin import VacancyAdmin
from resume.admin import ResumeAdmin, CandidateAdmin
from auth.admin import UserAdmin
from admin.auth_backend import AdminAuth

from auth.router import router as router_user
from resume.router import router as router_resume
from vacancy.router import router as router_vacancy


async def __init_admin():
    admin_settings = settings.admin
    admin = Admin(
        app=app,
        engine=engine,
        authentication_backend=AdminAuth(secret_key=admin_settings.SECRET_SESSION),
    )
    admin_views = [UserAdmin, ResumeAdmin, VacancyAdmin, CandidateAdmin]
    [admin.add_view(view) for view in admin_views]


async def __init_limiter():
    await FastAPILimiter.init(redis=redis_connection)


async def __close_limiter():
    await FastAPILimiter.close(redis=redis_connection)


async def start_up(app: FastAPI):
    logger.debug("App started")
    await __init_admin()
    await __init_limiter()


async def shut_down(app: FastAPI):
    logger.debug("Shutting down")
    await __close_limiter()


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
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


request_limiter_settings = settings.request_limiter
app.include_router(
    router_user, 
    tags=["auth"],
    dependencies=[Depends(request_limiter_settings.DEFAULT_LIMIT)],
)
app.include_router(
    fastapi_users.get_reset_password_router(), 
    tags=["auth"],
    dependencies=[Depends(request_limiter_settings.DEFAULT_LIMIT)],
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend), 
    tags=["auth"],
    dependencies=[Depends(request_limiter_settings.DEFAULT_LIMIT)],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate), 
    tags=["auth"],
    dependencies=[Depends(request_limiter_settings.DEFAULT_LIMIT)],
)
app.include_router(
    router_vacancy,
    prefix="/api/v1/vacancy",
    tags=["vacancy"],
    dependencies=[Depends(request_limiter_settings.DEFAULT_LIMIT)],
)
app.include_router(
    router_resume,
    prefix="/api/v1/resume",
    tags=["resume"],
    dependencies=[Depends(request_limiter_settings.DEFAULT_LIMIT)],
)
app.include_router(
    sse_router,
    prefix="/api/v1/sse",
    tags=["sse"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
