import enum

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# metadata = MetaData()


class Base(DeclarativeBase):
    pass


class WorkFormat(enum.Enum):
    office = 'in office'
    home = 'from home'
    hybrid = 'hybrid'
    discuss = 'discuss'


class WorkExperience(enum.Enum):
    no_experience = 'no experience'
    up_to_1_year = 'up to 1 year'
    between_1_and_3 = '1-3 years'
    between_3_and_6 = '3-6 years'
    more_than_6 = 'more than 6 years'


# vacancy = Table(
#     "vacancy",
#     metadata,
#     Column("id", Integer, nullable=False, primary_key=True),
#     Column("job_title", String, nullable=False),
#     Column("company", String, nullable=False),
#     Column("work_experience", String, nullable=False),
#     Column("work_format", String, nullable=False),
#     Column("salary", Integer),
#     Column("skills", String),
#     Column("about", Text, nullable=False),
# )


class Vacancy(Base):
    __tablename__ = "vacancy"

    id: Mapped[int] = mapped_column(primary_key=True)
    job_title: Mapped[str]
    company: Mapped[str]
    work_experience: Mapped[WorkExperience]
    work_format: Mapped[WorkFormat]
    salary: Mapped[int | None] = None
    skills: Mapped[str]  # TODO: change to list-like
    about: Mapped[str]
