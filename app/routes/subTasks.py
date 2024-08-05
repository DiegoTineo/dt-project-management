from fastapi import APIRouter, HTTPException, status
from app.config.db import conn
from app.data.models.subTask import SubTask as subtask_model

from sqlalchemy import select
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

sub_task_router = APIRouter()