from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

resume = Table(
    "resume",
    metadata,
    Column("id", Integer, nullable=False, primary_key=True),
    Column("job_title", String, nullable=False),
    Column("age", Integer, nullable=False),
    Column("sex", String, nullable=False),
    Column("birth_date", String, nullable=False),
    Column("lived_in", String, nullable=False),
    Column("want_salary", Integer),
    Column("status", String),
    Column("about", String),
)
