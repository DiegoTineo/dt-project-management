from fastapi import APIRouter, HTTPException, status
from app.config.db import conn
from app.data.models.taskStage import taskStage as task_stage_model

from sqlalchemy import select
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

task_stage_router = APIRouter()