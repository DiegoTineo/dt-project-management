from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer, String
from app.config.db import meta, engine

SubTask = Table(
    "sub_tasks",
    meta,
    Column("id", Integer, primary_key=True),
    Column("main_task_id", Integer, ForeignKey('tasks.id')),
    Column("sub_task_id", Integer, ForeignKey('tasks.id')),
)

meta.create_all(engine)
