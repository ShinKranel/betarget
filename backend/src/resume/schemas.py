from pydantic import BaseModel, AnyUrl, Field, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber

from resume.models import Gender, InterestInJob, ResumeStage



class CandidateCreate(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str | None = Field(None, max_length=50)
    age: int | None = Field(None, ge=0, le=130)
    gender: Gender | None
    city: str | None = Field(None, max_length=50)
    about: str | None = Field(None, max_length=2000)

    telegram: str | None = Field(None, max_length=60)
    whatsapp: str | None = Field(None, max_length=60)
    linkedin: str | None = Field(None, max_length=150)
    github: str | None = Field(None, max_length=150)
    email: EmailStr | None
    phone_number: PhoneNumber | None
    
    profile_picture: AnyUrl | None = Field(None)


class CandidateRead(BaseModel):
    id: int

    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str | None = Field(None, max_length=50)
    age: int | None = Field(None, ge=0, le=130)
    gender: Gender | None
    city: str | None = Field(None, max_length=50)
    about: str | None = Field(None, max_length=2000)

    telegram: AnyUrl | None
    whatsapp: AnyUrl | None
    linkedin: AnyUrl | None
    github: AnyUrl | None
    email: EmailStr | None
    phone_number: PhoneNumber | None
    
    profile_picture: AnyUrl | None = Field(None)


class CandidateUpdate(CandidateRead):
    pass


class ResumeCreate(BaseModel):
    resume_stage: ResumeStage = 'in_work'
    rating: int | None = Field(None, ge=0, le=10)

    # content
    job_title: str = Field(..., min_length=1, max_length=60)
    expected_salary: int | None = Field(None, ge=0)
    interest_in_job: InterestInJob | None
    skills: list[str] | None = Field(None, max_items=20)
    experience: str | None = Field(None, max_length=2000)
    education: str | None = Field(None, max_length=2000)
    ready_to_relocate: bool | None
    ready_for_business_trips: bool | None

    # Candidate information
    candidate: CandidateCreate = Field(...)


class ResumeRead(BaseModel):
    id: int
    resume_stage: ResumeStage
    rating: int | None = Field(None, ge=0, le=10)
    
    # content
    job_title: str = Field(..., min_length=1, max_length=60)
    expected_salary: int | None = Field(None, ge=0)
    interest_in_job: InterestInJob | None
    skills: list[str] | None = Field(None, max_items=20)
    experience: str | None = Field(None, max_length=2000)
    education: str | None = Field(None, max_length=2000)
    ready_to_relocate: bool | None
    ready_for_business_trips: bool | None

    # Candidate information
    candidate: CandidateRead = Field(...)


class ResumeUpdate(ResumeRead):
    pass
