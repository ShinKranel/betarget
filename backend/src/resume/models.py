import enum
from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.base import Base


# Enums ------------------------
class Sex(enum.Enum):
    male = 'male'
    female = 'female'
    other = 'other'


class InterestStatus(enum.Enum):
    """Candidate's job interest status"""
    looking_for_job = 'looking for job'
    not_looking_for_a_job = 'not looking for a job'
    considers_proposals = 'considers proposals'
    offered_a_job_decides = 'offered a job, decides'


# Models ------------------------
class Resume(Base):
    __tablename__ = "resume"

    id: Mapped[int] = mapped_column(primary_key=True)
    job_title: Mapped[str]
    age: Mapped[int | None]
    sex: Mapped[Sex]
    birth_date: Mapped[date | None] = None
    lived_in: Mapped[str | None] = None
    want_salary: Mapped[int]
    status: Mapped[InterestStatus]
    about: Mapped[str]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"), nullable=False, default=1
    )
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancy.id"), nullable=False, default=1
    )

    vacancy: Mapped["Vacancy"] = relationship(back_populates="resumes")
