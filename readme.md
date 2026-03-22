# FastAPI 101

A simple Todo REST API built with [FastAPI](https://fastapi.tiangolo.com/), SQLAlchemy, and PostgreSQL.

## Project Structure

```
app/
├── main.py               # App entry point
├── core/
│   └── config.py         # App configuration (loads DATABASE_URL from .env)
├── database/
│   ├── base.py           # SQLAlchemy declarative base
│   └── connection.py     # Database engine & session factory
├── dependencies/
│   └── db.py             # DB session dependency (get_db)
├── models/
│   └── todo.py           # SQLAlchemy TodoModel (id, title, completed)
├── routers/
│   └── todo.py           # Todo routes
├── schemas/
│   └── todo.py           # Pydantic schemas (TodoCreate, Todo)
└── services/
    └── todo_service.py   # Business logic (create, get_all, get_one)
docker-compose.yml        # PostgreSQL service
requirements.txt          # Python dependencies
```

## Requirements

- Python 3.10+
- Docker & Docker Compose (for the PostgreSQL database)
- Dependencies: `fastapi`, `pydantic`, `sqlalchemy`, `psycopg2-binary`, `python-dotenv`, `uvicorn`

## Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/fastapi_db
```

## Setup

### 1. Start the database

```bash
docker compose up -d
```

This starts a PostgreSQL 15 container (`fastapi-postgres`) on port `5432` with database `fastapi_db`.

### 2. Install Python dependencies

```bash
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the app

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Tables are created automatically on startup via SQLAlchemy.

## API Endpoints

| Method | Endpoint          | Description           | Request Body              |
|--------|-------------------|-----------------------|---------------------------|
| POST   | `/todos/`         | Create a todo         | `{ "title": "string" }`   |
| GET    | `/todos/`         | List all todos        | —                         |
| GET    | `/todos/{todo_id}`| Get a todo by ID      | —                         |

### Todo Schema

```json
{
  "id": 1,
  "title": "Buy groceries",
  "completed": false
}
```

## Interactive Docs

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
