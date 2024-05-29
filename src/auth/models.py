from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from sqlalchemy import Integer, String, Boolean, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.base import Base
from src.vacancy.models import Vacancy


# Models ------------------------
class User(SQLAlchemyBaseUserTable[int], Base):
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(
        Integer, unique=True, index=True, nullable=False, primary_key=True
    )
    username: Mapped[str] = mapped_column(
        String(length=10), unique=True
    )
    email: Mapped[str] = mapped_column(
        String(length=20), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    registered_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    vacancies: Mapped[list["Vacancy"]] = relationship(back_populates="user")
