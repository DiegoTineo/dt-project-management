from fastapi import APIRouter, HTTPException, status
from app.config.db import conn
from app.data.models.sprint import Sprint as sprint_model

from sqlalchemy import select
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

sprints_router = APIRouter()