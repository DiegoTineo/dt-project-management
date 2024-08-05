from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.config.db import conn

from app.data.models.organization import Organization as organization_model
from app.data.models.user import User as user_model

from app.data.schemas.organization import Organization as organization_schema

organizations_router = APIRouter()

@organizations_router.get("/organizations", tags=["organizations"])
def get_organizations():
    try:
        result = conn.execute(
            select(
                organization_model.c.id.label("organization_id"),
                organization_model.c.name.label("organization_name"),
                organization_model.c.user_id.label("organization_user_id"),
                organization_model.c.created_at,
                user_model.c.id.label("user_id"),
                user_model.c.name.label("user_name"),
                user_model.c.email,
            ).select_from(
                organization_model.join(
                    user_model,
                    organization_model.c.user_id == user_model.c.id,
                    isouter=True,
                )
            )
        )
        organizations_with_users = [dict(row._mapping) for row in result]

        return organizations_with_users

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
