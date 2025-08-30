# app/schemas.py
from pydantic import BaseModel
from typing import Optional

# Request model for creating a task
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Request model for updating a task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Response model for returning task data
class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    class Config:
        orm_mode = True
