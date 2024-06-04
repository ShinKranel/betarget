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