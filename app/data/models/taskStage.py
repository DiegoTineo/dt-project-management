from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer, String
from app.config.db import meta, engine

taskStage = Table(
    "task_stages",
    meta,    
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("project_id", Integer, ForeignKey('projects.id')),
)

meta.create_all(engine)
