import enum

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.base import Base


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
    skills: Mapped[str]  # TODO: change to list-like
    description: Mapped[str]

    # foreign keys
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"), nullable=False, default=None)

    # relationships
    resumes = relationship("Resume", back_populates="vacancy")
    main_user = relationship("User", back_populates="vacancies")
