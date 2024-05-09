import enum
from datetime import date

from sqlalchemy import Table, Column, Integer, String, MetaData, Date, Text, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from src.auth.models import user

metadata = MetaData()


class Base(DeclarativeBase):
    pass


class Sex(enum.Enum):
    male = 'male'
    female = 'female'
    other = 'other'


class InterestStatus(enum.Enum):
    """Candidate's job interest status"""
    looking_for_job = 'looking for job'
    not_looking_for_a_job = 'not looking for a job'
    considers_proposals = 'considers proposals'
    offered_a_job_decides = 'offered a job, decides'


resume = Table(
    "resume",
    metadata,
    Column("id", Integer, nullable=False, primary_key=True),
    Column("user_id", ForeignKey(user.c.id)),
    Column("job_title", String, nullable=False),
    Column("age", Integer),
    Column("sex", Enum(Sex)),
    Column("birth_date", Date),
    Column("lived_in", String),
    Column("want_salary", Integer,),
    Column("status", Enum(InterestStatus)),
    Column("about", Text),
)


class Resume(Base):
    __tablename__ = "resume"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[ForeignKey(user.c.id)] = mapped_column(
        ForeignKey(user.c.id), nullable=False)
    job_title: Mapped[str]
    age: Mapped[int | None]
    sex: Mapped[Sex]
    birth_date: Mapped[date | None] = None
    lived_in: Mapped[str | None] = None
    want_salary: Mapped[int]
    status: Mapped[InterestStatus]
    about: Mapped[str]
