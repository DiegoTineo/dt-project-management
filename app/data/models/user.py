from sqlalchemy import Column, DateTime, Table
from sqlalchemy.sql.sqltypes import Integer, String
from app.config.db import meta, engine

User = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
    Column("firstName", String(255)),
    Column("lastName", String(255)),
    
    Column("createAt", DateTime),
    Column("updatedAt", DateTime),
)

meta.create_all(engine)
