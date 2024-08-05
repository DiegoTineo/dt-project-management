from fastapi import APIRouter, HTTPException, status
from app.config.db import conn
from app.data.models.project import Projects as project_model

from sqlalchemy import select
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

projects_router = APIRouter()