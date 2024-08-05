from fastapi import APIRouter, HTTPException, status
from app.config.db import conn
from app.data.models.user import User as user_model
from app.data.schemas.user import User as user_schema
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import select
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

users_router = APIRouter()

@users_router.get("/users", tags=["users"])
def get_users():
    try:
        result = conn.execute(
             select(user_model)
        )
        users_list = [dict(row._mapping) for row in result]
        return users_list
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))