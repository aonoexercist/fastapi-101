from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str

class Todo(TodoCreate):
    id: int
    completed: bool

    class Config:
        from_attributes = True