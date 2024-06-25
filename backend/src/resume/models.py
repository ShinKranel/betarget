import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.base import Base


# Enums ------------------------
class Gender(enum.Enum):
    male = 'male'
    female = 'female'
    other = 'other'


class InterestInJob(enum.Enum):
    """Candidate's job interest status"""
    looking_for_job = 'looking for job'
    not_looking_for_a_job = 'not looking for a job'
    considers_proposals = 'considers proposals'
    offered_a_job_decides = 'offered a job, decides'


class ResumeStatus(enum.Enum):
    in_work = 'in_work'
    screening = 'screening'
    interview = 'interview'
    review = 'review'
    accepted = 'accepted'
    rejected = 'rejected'
    offer = 'offer'


# Models ------------------------
class Resume(Base):
    __tablename__ = "resume"

    id: Mapped[int] = mapped_column(primary_key=True)

    resume_status: Mapped[ResumeStatus]
    rating: Mapped[int | None] = None
    first_name: Mapped[str]
    job_title: Mapped[str]
    last_name: Mapped[str]
    age: Mapped[int | None] = None
    gender: Mapped[Gender | None] = None
    city: Mapped[str | None] = None
    expected_salary: Mapped[int | None] = None
    interest_in_job: Mapped[InterestInJob | None] = None
    skills: Mapped[str | None] = None
    about: Mapped[str | None] = None
    experience: Mapped[str | None] = None
    education: Mapped[str | None] = None
    ready_to_relocate: Mapped[bool | None] = None
    ready_for_business_trips: Mapped[bool | None] = None

    # foreign keys
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancy.id", ondelete="CASCADE"), nullable=False
    )

    # relationships
    vacancy = relationship("Vacancy", back_populates="resumes")
    user = relationship("User", back_populates="resumes")
