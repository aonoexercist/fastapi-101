from app.schemas.todo import Todo

todos = []

def create_todo(todo: Todo):
    todos.append(todo)
    return todo

def get_all():
    return todos

def get_one(todo_id: int):
    for t in todos:
        if t.id == todo_id:
            return t
    return None