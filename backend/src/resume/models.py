import enum

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, relationship, mapped_column

from base import Base


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
    job_title: Mapped[str]
    expected_salary: Mapped[int | None]
    interest_in_job: Mapped[InterestInJob | None]
    skills: Mapped[ARRAY | None] = mapped_column(ARRAY(String(255)))
    experience: Mapped[str | None]
    education: Mapped[str | None]
    ready_to_relocate: Mapped[bool | None]
    ready_for_business_trips: Mapped[bool | None]

    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancy.id", ondelete="CASCADE"), nullable=False
    )
    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("candidate.id"), nullable=False
    )

    # relationships
    vacancy = relationship("Vacancy", back_populates="resumes")
    candidate = relationship("Candidate", back_populates="resume", lazy="joined")

    def __doc__(self):
        return f"Resume({self.id}) {self.job_title}"
    
    def __str__(self):
        return f"({self.id}) {self.job_title}"


class Candidate(Base):
    __tablename__ = "candidate"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    age: Mapped[int | None]
    gender: Mapped[Gender | None]
    city: Mapped[str | None]
    about: Mapped[str | None]

    # contacts
    telegram: Mapped[str | None] = mapped_column(String, nullable=True)
    whatsapp: Mapped[str | None] = mapped_column(String, nullable=True)
    linkedin: Mapped[str | None] = mapped_column(String, nullable=True)
    github: Mapped[str | None] = mapped_column(String, nullable=True)
    email: Mapped[str | None]
    phone_number: Mapped[str | None]

    profile_picture: Mapped[str | None]  = mapped_column(String, nullable=True)

    # relationships
    resume = relationship("Resume", back_populates="candidate", cascade="all, delete", lazy="joined")

    def __doc__(self):
        return f"Candidate({self.id}) {self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"({self.id}) {self.first_name} {self.last_name}"