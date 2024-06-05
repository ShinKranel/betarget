from pydantic import BaseModel

from backend.src.vacancy.models import WorkFormat, Experience, Education, EmploymentType


class CreateVacancy(BaseModel):
    job_title: str
    city: str
    company: str
    experience: Experience
    work_format: WorkFormat
    salary: int
    education: Education
    employment_type: EmploymentType
    skills: str
    description: str

    user_id: int = 1


class ReadVacancy(BaseModel):
    job_title: str
    city: str
    company: str
    experience: Experience
    work_format: WorkFormat
    salary: int
    education: Education
    employment_type: EmploymentType
    skills: str
    description: str


class UpdateVacancy(BaseModel):
    job_title: str | None
    city: str | None
    company: str | None
    experience: Experience | None
    work_format: WorkFormat | None
    salary: int | None
    education: Education | None
    employment_type: EmploymentType | None
    skills: str | None
    description: str | None
