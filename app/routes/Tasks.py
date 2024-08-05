from fastapi import APIRouter, HTTPException, status
from app.config.db import conn
from app.data.models.task import task as task_model

from sqlalchemy import select
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

task_router = APIRouter()