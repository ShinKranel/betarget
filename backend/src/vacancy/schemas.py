from datetime import datetime

from pydantic import BaseModel, Field, UUID4

from vacancy.models import WorkFormat, Experience, Education, EmploymentType


class VacancyCreate(BaseModel):
    job_title: str = Field(..., min_length=1, max_length=60)
    city: str | None = Field(None, max_length=50)
    company: str = Field(..., min_length=1, max_length=50)
    experience: Experience | None
    work_format: WorkFormat | None
    salary: int | None = Field(None, ge=0)
    education: Education | None
    employment_type: EmploymentType | None
    skills: list[str] | None = Field(None, max_items=20)
    description: str | None = Field(None, max_length=2000)


class VacancyRead(BaseModel):
    id: int
    user_id: UUID4
    job_title: str | None = Field(None, min_length=1, max_length=60)
    city: str | None = Field(None, max_length=50)
    company: str = Field(..., min_length=1, max_length=50)
    experience: Experience | None
    work_format: WorkFormat | None
    salary: int | None = Field(None, ge=0)
    education: Education | None
    employment_type: EmploymentType | None
    skills: list[str] | None = Field(None, max_items=20)
    description: str | None = Field(None, max_length=2000)
    created_at: datetime
    expiration_date: datetime


class VacancyUpdate(VacancyRead):
    pass