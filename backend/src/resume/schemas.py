from pydantic import BaseModel, Field, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

from backend.src.resume.models import Gender, InterestInJob, ResumeStage


class ResumeCreate(BaseModel):
    resume_stage: ResumeStage = 'in_work'
    rating: int | None = Field(None, ge=0, le=10)

    # content
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str | None = Field(None, max_length=50)
    job_title: str = Field(..., min_length=1, max_length=60)
    age: int | None = Field(None, ge=0, le=130)
    gender: Gender | None
    city: str | None = Field(None, max_length=50)
    expected_salary: int | None = Field(None, ge=0)
    interest_in_job: InterestInJob | None
    skills: list[str] | None = Field(None, max_items=20)
    about: str | None = Field(None, max_length=2000)
    experience: str | None = Field(None, max_length=2000)
    education: str | None = Field(None, max_length=2000)
    ready_to_relocate: bool | None
    ready_for_business_trips: bool | None

    # contacts
    telegram: str | None = Field(None, max_length=60)
    whatsapp: str | None = Field(None, max_length=60)
    linkedin: str | None = Field(None, max_length=150)
    github: str | None = Field(None, max_length=150)
    email: EmailStr | None
    phone_number: PhoneNumber | None


class ResumeRead(BaseModel):
    id: int
    resume_stage: ResumeStage
    rating: int | None = Field(None, ge=0, le=10)

    # content
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(None, min_length=1, max_length=50)
    job_title: str = Field(..., min_length=1, max_length=60)
    age: int | None = Field(None, ge=0, le=130)
    gender: Gender | None
    city: str | None = Field(None, max_length=50)
    expected_salary: int | None = Field(None, ge=0)
    interest_in_job: InterestInJob | None
    skills: list[str] | None = Field(None, max_items=20)
    about: str | None = Field(None, max_length=2000)
    experience: str | None = Field(None, max_length=2000)
    education: str | None = Field(None, max_length=2000)
    ready_to_relocate: bool | None
    ready_for_business_trips: bool | None

    # contacts
    telegram: str | None = Field(None, max_length=60)
    whatsapp: str | None = Field(None, max_length=60)
    linkedin: str | None = Field(None, max_length=150)
    github: str | None = Field(None, max_length=150)
    email: EmailStr | None
    phone_number: PhoneNumber | None


class ResumeUpdate(ResumeRead):
    pass