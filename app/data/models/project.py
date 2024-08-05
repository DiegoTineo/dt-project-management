from sqlalchemy import Column, DateTime, ForeignKey, Table
from app.config.db import meta, engine
from sqlalchemy.sql.sqltypes import Integer, String

Projects = Table(
    "projects",
    meta,
    Column("id", Integer, primary_key=True),
    
    Column("name", String(255)),
    Column("description", String(255)),
    Column("organization_id", Integer, ForeignKey('organizations.id')),
    
    Column("created_at", DateTime),
    Column("init_date", DateTime),
    Column("end_date", DateTime),
    Column("updated_at", DateTime),
    Column("finished_at", DateTime),
    
    Column("user_id", Integer, ForeignKey('users.id')),
    Column("finished", Integer),
)

meta.create_all(engine)
