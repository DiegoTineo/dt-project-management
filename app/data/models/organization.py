from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from app.config.db import meta, engine

Organization = Table(
    "organizations",
    meta,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(255)),
    Column("user_id", Integer, ForeignKey('users.id')),
    Column("created_at", DateTime),
)

meta.create_all(engine)
