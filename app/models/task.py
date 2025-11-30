from typing import Optional
from pydantic import BaseModel

from app.models.user import User

class Task(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    completed: Optional[bool] = False
    created_by: str

class TaskUpdate(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = False
    created_by: Optional[str] = None