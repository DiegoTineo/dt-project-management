from sqlalchemy import Column, DateTime, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer, String
from app.config.db import meta, engine

task = Table(
    "tasks",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("project_id", Integer, ForeignKey('projects.id')),
    Column("sprint_id", Integer, ForeignKey('sprints.id')),

    Column("created_at", DateTime),
    Column("init_date", DateTime),
    Column("end_date", DateTime),
    Column("updated_at", DateTime),
    Column("finished_at", DateTime),
    
    Column("finished", Integer),
    
)

meta.create_all(engine)
