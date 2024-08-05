from fastapi import APIRouter, HTTPException, status
from app.config.db import conn
from app.data.models.userOrganization import userOrganization as user_organization_model

from sqlalchemy import select
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user_organization_router = APIRouter()