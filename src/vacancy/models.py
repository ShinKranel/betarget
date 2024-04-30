from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

vacancy = Table(
    "vacancy",
    metadata,
    Column("id", Integer, nullable=False, primary_key=True),
    Column("job_title", String, nullable=False),
    Column("company", String, nullable=False),
    Column("work_experience", Integer, nullable=False),
    Column("work_format", String, nullable=False),
    Column("salary", Integer),
    Column("skills", Integer),
    Column("about", Integer, nullable=False),
)
