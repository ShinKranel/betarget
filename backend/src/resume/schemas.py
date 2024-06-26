from pydantic import BaseModel, Field, EmailStr

from backend.src.resume.models import Gender, ResumeStatus, InterestInJob
# from pydantic_extra_types.phone_numbers import PhoneNumber


class ResumeCreate(BaseModel):
    resume_status: ResumeStatus = 'in_work'
    rating: int | None = Field(None, ge=0, le=10)

    # content
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
    email: EmailStr = None
    phone_number: str = None


class ResumeRead(BaseModel):
    resume_status: ResumeStatus
    rating: int | None

    # content
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

    # contacts
    telegram: str | None
    whatsapp: str | None
    linkedin: str | None
    github: str | None
    email: EmailStr | None
    phone_number: str | None
