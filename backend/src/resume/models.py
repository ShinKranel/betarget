import enum
from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.base import Base


# Enums ------------------------
class Gender(enum.Enum):
    male = 'male'
    female = 'female'
    other = 'other'


class ResumeStatus(enum.Enum):
    """Candidate's job interest status"""
    looking_for_job = 'looking for job'
    not_looking_for_a_job = 'not looking for a job'
    considers_proposals = 'considers proposals'
    offered_a_job_decides = 'offered a job, decides'


# Models ------------------------
class Resume(Base):
    __tablename__ = "resume"

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str]
    job_title: Mapped[str]
    last_name: Mapped[str]
    age: Mapped[int | None]
    gender: Mapped[Gender]
    city: Mapped[str | None] = None
    expected_salary: Mapped[int | None]
    resume_status: Mapped[ResumeStatus]
    skills: Mapped[str | None]
    about: Mapped[str]
    experience: Mapped[str]
    education: Mapped[str]
    ready_to_relocate: Mapped[bool | None]
    ready_for_business_trips: Mapped[bool | None]

    # foreign keys
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"), nullable=False,
    )
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancy.id"), nullable=False
    )

    # relationships
    vacancy: Mapped["Vacancy"] = relationship(back_populates="resumes")
