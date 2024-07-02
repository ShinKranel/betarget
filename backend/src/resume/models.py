import enum

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import ARRAY
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


class ResumeStage(enum.Enum):
    in_work = 'in_work'
    screening = 'screening'
    interview = 'interview'
    rejected = 'rejected'
    offer = 'offer'


# Models ------------------------
class Resume(Base):
    __tablename__ = "resume"

    id: Mapped[int] = mapped_column(primary_key=True)

    resume_stage: Mapped[ResumeStage]
    rating: Mapped[int | None] = None

    # content
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    job_title: Mapped[str]
    age: Mapped[int | None]
    gender: Mapped[Gender | None]
    city: Mapped[str | None]
    expected_salary: Mapped[int | None]
    interest_in_job: Mapped[InterestInJob | None]
    skills: Mapped[ARRAY | None] = mapped_column(ARRAY(String(255)))
    about: Mapped[str | None]
    experience: Mapped[str | None]
    education: Mapped[str | None]
    ready_to_relocate: Mapped[bool | None]
    ready_for_business_trips: Mapped[bool | None]

    # contacts
    telegram: Mapped[str | None]
    whatsapp: Mapped[str | None]
    linkedin: Mapped[str | None]
    github: Mapped[str | None]
    email: Mapped[str | None]
    phone_number: Mapped[str | None]  # todo: change to PhoneNumber

    # TODO: add photo field

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
