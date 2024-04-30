from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()


user = Table(
    "user",
    metadata,
    Column("id", Integer, nullable=False, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", String, nullable=False),
)
