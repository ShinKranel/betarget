import enum
from datetime import datetime

from sqlalchemy import ForeignKey, String, text
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from config import settings

from base import Base


# Enums ------------------------
class WorkFormat(enum.Enum):
    office = 'in office'
    home = 'from home'
    hybrid = 'hybrid'
    discuss = 'discuss'


class Experience(enum.Enum):
    no_experience = 'no experience'
    up_to_1_year = 'up to 1 year'
    between_1_and_3 = '1-3 years'
    between_3_and_6 = '3-6 years'
    more_than_6 = 'more than 6 years'


class EmploymentType(enum.Enum):
    full_time = "full_time"
    part_time = "part_time"
    internship = "internship"
    volunteer = "volunteer"


class Education(enum.Enum):
    incomplete_secondary = "incomplete_secondary"
    secondary = "secondary"
    secondary_vocational = "secondary_vocational"
    incomplete_higher = "incomplete_higher"
    bachelor = "bachelor"
    master = "master"
    phd = "phd"


# Models ------------------------
class Vacancy(Base):
    __tablename__ = "vacancy"

    id: Mapped[int] = mapped_column(primary_key=True)

    job_title: Mapped[str] = mapped_column(String(length=60))
    city: Mapped[str] = mapped_column(String(length=50))
    company: Mapped[str] = mapped_column(String(length=50))
    experience: Mapped[Experience]
    work_format: Mapped[WorkFormat]
    salary: Mapped[int | None] = None
    education: Mapped[Education | None] = None
    employment_type: Mapped[EmploymentType]
    skills: Mapped[ARRAY] = mapped_column(ARRAY(String(255)))
    description: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    expiration_date: Mapped[datetime] = mapped_column(
        server_default=text(f"TIMEZONE('utc', now() + INTERVAL '{settings.vacancy.EXPIRATION_TIME} day')")
    )

    # foreign keys
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    # relationships
    resumes = relationship("Resume", back_populates="vacancy", cascade="all, delete", passive_deletes=True)
    user = relationship("User", back_populates="vacancies")

    def __doc__(self):
        return f"Vacancy({self.id}){self.job_title} | {self.company}"

    def __str__(self):
        return f"({self.id}) {self.job_title} | {self.company}"
