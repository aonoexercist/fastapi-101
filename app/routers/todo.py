from fastapi import APIRouter, HTTPException
from app.schemas.todo import Todo
from app.services import todo_service

router = APIRouter()

@router.post("/")
def create(todo: Todo):
    return todo_service.create_todo(todo)

@router.get("/")
def get_all():
    return todo_service.get_all()

@router.get("/{todo_id}")
def get_one(todo_id: int):
    todo = todo_service.get_one(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
    return todo