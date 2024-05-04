from sqlalchemy import Table, Column, Integer, String, MetaData, Enum, Text

metadata = MetaData()


class WorkFormat(Enum):
    office = 'in office'
    home = 'from home'
    hybrid = 'hybrid'


class WorkExperience(Enum):
    no_experience = 'no experience'
    up_to_1_year = 'up to 1 year'
    between_1_and_3 = '1-3 years'
    between_3_and_6 = '3-6 years'
    more_than_6 = 'more than 6 years'


vacancy = Table(
    "vacancy",
    metadata,
    Column("id", Integer, nullable=False, primary_key=True),
    Column("job_title", String, nullable=False),
    Column("company", String, nullable=False),
    Column("work_experience", Enum(WorkExperience), nullable=False),
    Column("work_format", Enum(WorkFormat), nullable=False),
    Column("salary", Integer),
    Column("skills", String),  # TODO: change to list-like
    Column("about", Text, nullable=False),
)
