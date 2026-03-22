# FastAPI 101

A simple Todo REST API built with [FastAPI](https://fastapi.tiangolo.com/).

## Project Structure

```
app/
├── main.py               # App entry point
├── core/
│   └── config.py         # App configuration
├── database/
│   ├── base.py           # SQLAlchemy base
│   └── connection.py     # Database connection
├── dependencies/
│   └── db.py             # DB session dependency
├── models/
│   └── todo.py           # SQLAlchemy model
├── routers/
│   └── todo.py           # Todo routes
├── schemas/
│   └── todo.py           # Pydantic schemas
└── services/
    └── todo_service.py   # Business logic
```

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

## Setup

```bash
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

## Running the App

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

| Method | Endpoint        | Description        |
|--------|-----------------|--------------------|
| GET    | `/`             | Health check       |
| POST   | `/todos/`       | Create a todo      |
| GET    | `/todos/`       | List all todos     |
| GET    | `/todos/{id}`   | Get a todo by ID   |

## Interactive Docs

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
