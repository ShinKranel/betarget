from sqlalchemy import Table, Column, Integer, String, MetaData, Date, Text, Enum

metadata = MetaData()


class Sex(Enum):
    male = 'male'
    female = 'female'
    other = 'other'


class InterestStatus(Enum):
    """Candidate's job interest status"""
    looking_for_job = 'looking for job'
    not_looking_for_a_job = 'not looking for a job'
    considers_proposals = 'considers proposals'
    offered_a_job_decides = 'offered a job, decides'


resume = Table(
    "resume",
    metadata,
    Column("id", Integer, nullable=False, primary_key=True),
    Column("job_title", String, nullable=False),
    Column("age", Integer, nullable=False),
    Column("sex", Enum(Sex), nullable=False),
    Column("birth_date", Date, nullable=False),
    Column("lived_in", String, nullable=False),
    Column("want_salary", Integer),
    Column("status", Enum(InterestStatus)),
    Column("about", Text),
)
