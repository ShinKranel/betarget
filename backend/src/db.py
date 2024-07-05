from typing import AsyncGenerator
from time import time

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.engine import Connection
from sqlalchemy.engine.interfaces import DBAPICursor, _DBAPIAnyExecuteParams
from sqlalchemy.engine.interfaces import ExecutionContext

from auth.models import User
from config import settings
from logger import db_query_logger


db_settings = settings.database

engine = create_async_engine(db_settings.DATABASE_URL_ASYNC)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(
    conn: Connection,
    cursor: DBAPICursor,
    statement: str,
    parameters: _DBAPIAnyExecuteParams,
    context: ExecutionContext | None,
    executemany: bool,
) -> None:
    context._query_start_time = time()
    db_query_logger.debug("Start Query:\n%s" % statement)
    db_query_logger.debug("Parameters:\n%r" % (parameters,))


@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(
    conn: Connection,
    cursor: DBAPICursor,
    statement: str,
    parameters: _DBAPIAnyExecuteParams,
    context: ExecutionContext,
    executemany: bool,
) -> None:
    total = time() - context._query_start_time
    db_query_logger.debug("Query Complete!\n\n")
    db_query_logger.debug("Total Time: %.02fms" % (total * 1000))


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)  #
