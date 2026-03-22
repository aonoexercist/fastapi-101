from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.todo import TodoCreate
from app.services import todo_service
from app.dependencies.db import get_db

router = APIRouter()

@router.post("/")
def create(todo: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo(db, todo)

@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return todo_service.get_all(db)

@router.get("/{todo_id}")
def get_one(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_service.get_one(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
    return todo