from datetime import datetime
import uuid

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from base import Base


# Models ------------------------
class User(SQLAlchemyBaseUserTable[uuid.UUID], Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), unique=True, index=True, nullable=False, primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(
        String(30), unique=True
    )
    email: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(1023), nullable=False
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

    # contacts
    telegram: Mapped[str | None] = mapped_column(String, nullable=True, default="https://example.com")
    whatsapp: Mapped[str | None] = mapped_column(String, nullable=True, default="https://example.com")
    linkedin: Mapped[str | None] = mapped_column(String, nullable=True, default="https://example.com")
    github: Mapped[str | None] = mapped_column(String, nullable=True, default="https://example.com")
    email: Mapped[str | None] 
    phone_number: Mapped[str | None]
    verification_token: Mapped[str | None]
    reset_password_token: Mapped[str | None]

    profile_picture: Mapped[str | None] = mapped_column(String, nullable=True, default="https://example.com")

    vacancies = relationship("Vacancy", back_populates="user", cascade="all, delete", passive_deletes=True)

    def __doc__(self):
        return f"User({self.id}){self.username}"

    def __str__(self):
        return f"({self.id}) {self.username}"
