from pydantic import BaseModel

from src.vacancy.models import WorkExperience, WorkFormat


class CreateVacancy(BaseModel):
    job_title: str
    company: str
    work_experience: WorkExperience
    work_format: WorkFormat
    salary: int | None = None
    skills: str | None = None  # TODO: change to list-like
    about: str
