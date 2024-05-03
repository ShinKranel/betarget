from sqlalchemy import Table, Column, Integer, String, MetaData, Date, Text, Enum

metadata = MetaData()

class Sex(Enum):
    male = 'male'
    female = 'female'
    other = 'other'

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
    Column("status", String),
    Column("about", Text),
)
