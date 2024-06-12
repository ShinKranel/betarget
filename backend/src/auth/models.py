from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from sqlalchemy import Integer, String, Boolean, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.base import Base


# Models ------------------------
class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        Integer, unique=True, index=True, nullable=False, primary_key=True
    )
    username: Mapped[str] = mapped_column(
        String(length=30), unique=True
    )
    email: Mapped[str] = mapped_column(
        String(length=50), unique=True, index=True, nullable=False
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

    vacancies = relationship("Vacancy", back_populates="user", cascade="all, delete", passive_deletes=True)
    resumes = relationship("Resume", back_populates="user", cascade="all, delete", passive_deletes=True)
