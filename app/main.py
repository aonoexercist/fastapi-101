from fastapi import FastAPI
from app.routers import todo

app = FastAPI()

app.include_router(todo.router, prefix="/todos", tags=["todos"])

@app.get("/")
def root():
    return {"message": "Todo API is running 🚀"}