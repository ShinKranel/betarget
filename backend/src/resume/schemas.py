from pydantic import BaseModel, Field, EmailStr

from backend.src.resume.models import Gender, InterestInJob, ResumeStage
# from pydantic_extra_types.phone_numbers import PhoneNumber


# todo: add restrictions to every param
class ResumeCreate(BaseModel):
    resume_stage: ResumeStage = 'in_work'
    rating: int | None = Field(None, ge=0, le=10)

    # content
    first_name: str
    last_name: str | None
    job_title: str
    age: int | None = Field(None, ge=0, le=130)
    gender: Gender | None
    city: str | None
    expected_salary: int | None
    interest_in_job: InterestInJob | None
    skills: list[str] | None
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
    phone_number: str | None  # todo: change to pydantic_extra_types.phone_numbers.PhoneNumber in production ver


class ResumeRead(BaseModel):
    id: int
    resume_stage: ResumeStage
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
    skills: list[str] | None
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
    phone_number: str | None  # TODO: change to pydantic_extra_types.phone_numbers.PhoneNumber in production ver


class ResumeUpdate(ResumeRead):
    pass