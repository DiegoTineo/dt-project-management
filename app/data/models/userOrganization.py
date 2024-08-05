from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import Integer, String
from app.config.db import meta, engine

userOrganization = Table(
    "user_organizations",
    meta,
    Column("id", Integer, primary_key=True),
    Column("user_id", String(255)),
    Column("organization_id", Integer, ForeignKey('organizations.id')),
)

meta.create_all(engine)
