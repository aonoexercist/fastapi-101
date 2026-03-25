from pydantic import BaseModel
from typing import Optional

class TodoCreate(BaseModel):
    title: str

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TodoDelete(BaseModel):
    id: int

class Todo(TodoCreate):
    id: int
    completed: bool

    class Config:
        from_attributes = True