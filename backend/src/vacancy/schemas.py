from pydantic import BaseModel

from backend.src.vacancy.models import WorkFormat, Experience, Education, EmploymentType


# todo: add restrictions to every param
class VacancyCreate(BaseModel):
    job_title: str
    city: str | None
    company: str
    experience: Experience | None
    work_format: WorkFormat | None
    salary: int | None
    education: Education | None
    employment_type: EmploymentType | None
    skills: list[str] | None
    description: str | None


class VacancyRead(BaseModel):
    id: int
    user_id: int
    job_title: str | None
    city: str | None
    company: str
    experience: Experience | None
    work_format: WorkFormat | None
    salary: int | None
    education: Education | None
    employment_type: EmploymentType | None
    skills: list[str] | None
    description: str | None


class VacancyUpdate(VacancyCreate):
    pass
