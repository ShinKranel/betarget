import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.base import Base

from src.resume.models import Resume


# Enums ------------------------
class WorkFormat(enum.Enum):
    office = 'in office'
    home = 'from home'
    hybrid = 'hybrid'
    discuss = 'discuss'


class WorkExperience(enum.Enum):
    no_experience = 'no experience'
    up_to_1_year = 'up to 1 year'
    between_1_and_3 = '1-3 years'
    between_3_and_6 = '3-6 years'
    more_than_6 = 'more than 6 years'


# Models ------------------------
class Vacancy(Base):
    __tablename__ = "vacancy"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"), nullable=False, default=1)
    job_title: Mapped[str]
    company: Mapped[str]
    work_experience: Mapped[WorkExperience]
    work_format: Mapped[WorkFormat]
    salary: Mapped[int | None] = None
    skills: Mapped[str]  # TODO: change to list-like
    about: Mapped[str]

    resumes: Mapped[list["Resume"]] = relationship(back_populates="vacancy")
    user: Mapped["User"] = relationship(back_populates="vacancies")

