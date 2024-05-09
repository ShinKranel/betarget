from datetime import date

from pydantic import BaseModel
from sqlalchemy import Date

from src.resume.models import Sex, InterestStatus


class CreateResume(BaseModel):
    job_title: str
    age: int
    sex: Sex
    birth_date: date
    lived_in: str
    want_salary: int
    status: InterestStatus
    about: str
