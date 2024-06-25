from pydantic import BaseModel, Field

from backend.src.resume.models import Gender, ResumeStatus, InterestInJob
from pydantic_extra_types.phone_numbers import PhoneNumber


class ResumeCreate(BaseModel):
    resume_status: ResumeStatus = 'in_work'
    rating: int = Field(None, ge=1, le=10)
    first_name: str
    last_name: str
    job_title: str
    age: int = Field(None, ge=0, le=130)
    gender: Gender = None
    city: str = None
    expected_salary: int = None
    interest_in_job: InterestInJob = None
    skills: str = None
    about: str = None
    experience: str = None
    education: str = None
    ready_to_relocate: bool = False
    ready_for_business_trips: bool = False

    # contacts
    telegram: str = None
    whatsapp: str = None
    linkedin: str = None
    github: str = None
    phone_number: PhoneNumber

    # photo


class ResumeRead(BaseModel):
    resume_status: ResumeStatus
    rating: int
    first_name: str
    last_name: str
    job_title: str
    age: int | None
    gender: Gender | None
    city: str | None
    expected_salary: int | None
    interest_in_job: InterestInJob | None
    skills: str | None
    about: str | None
    experience: str | None
    education: str | None
    ready_to_relocate: bool | None
    ready_for_business_trips: bool | None
