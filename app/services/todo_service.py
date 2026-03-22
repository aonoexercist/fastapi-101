from sqlalchemy.orm import Session
from app.models.todo import TodoModel
from app.schemas.todo import TodoCreate

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