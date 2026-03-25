from sqlalchemy.orm import Session
from app.models.todo import TodoModel
from app.schemas.todo import TodoCreate, TodoUpdate, Todo

def create_todo(db: Session, todo: TodoCreate):
    db_todo = TodoModel(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_all(db: Session):
    return db.query(TodoModel).all()

def get_one(db: Session, todo_id: int):
    return db.query(TodoModel).filter(TodoModel.id == todo_id).first()

def update_todo(db: Session, todo_id: int, updated: TodoUpdate):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()

    if not todo:
        return None

    if updated.title is not None:
        todo.title = updated.title

    if updated.completed is not None:
        todo.completed = updated.completed

    db.commit()
    db.refresh(todo)

    return todo

def delete_todo(db: Session, todo_id: int):
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()

    if not todo:
        return None

    db.delete(todo)
    db.commit()

    return True
