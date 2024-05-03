from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, MetaData, Boolean, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

metadata = MetaData()


user = Table(
    "user",
    metadata,
    Column("id", Integer, nullable=False, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, nullable=False),
    Column("is_superuser", Boolean, nullable=False),
    Column("is_verified", Boolean, nullable=False),
)


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(
        Integer, unique=True, index=True, nullable=False, primary_key=True
    )
    username: Mapped[str] = mapped_column(
        String(length=320), unique=True
    )
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    registered_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP, nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
