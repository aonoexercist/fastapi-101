from fastapi import FastAPI
from app.database.base import Base
from app.database.connection import engine
from app.routers import todo

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(todo.router, prefix="/todos", tags=["Todos"])


# @app.get("/")
# def root():
#     return {"message": "API is running 🚀"}