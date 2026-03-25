from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.todo import Todo, TodoCreate, TodoUpdate
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

@router.put("/{todo_id}", response_model=Todo)
def update(todo_id: int, updated: TodoUpdate, db: Session = Depends(get_db)):
    todo = todo_service.update_todo(db, todo_id, updated)
    
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
    
    return todo

@router.delete("/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)):
    success = todo_service.delete_todo(db, todo_id)

    if not success:
        raise HTTPException(status_code=404, detail="Not found")

    return {"message": "Deleted successfully"}