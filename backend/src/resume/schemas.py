from datetime import date

from pydantic import BaseModel

from backend.src.resume.models import Gender, ResumeStatus, InterestInJob


class ResumeCreate(BaseModel):
    resume_status: ResumeStatus = 'in_work'
    first_name: str
    last_name: str
    job_title: str
    age: int
    gender: Gender
    city: str
    expected_salary: int
    interest_in_job: InterestInJob
    skills: str
    about: str
    experience: str
    education: str
    ready_to_relocate: bool
    ready_for_business_trips: bool


class ResumeRead(BaseModel):
    resume_status: ResumeStatus
    first_name: str
    last_name: str
    job_title: str
    age: int
    gender: Gender
    city: str
    expected_salary: int
    interest_in_job: InterestInJob
    skills: str
    about: str
    experience: str
    education: str
    ready_to_relocate: bool
    ready_for_business_trips: bool
