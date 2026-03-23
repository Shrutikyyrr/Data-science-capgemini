# Section 1 – Backend API (FastAPI)

## Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoints
| Method | URL | Description |
|--------|-----|-------------|
| GET | /students | Get all students |
| GET | /students?course=AI | Filter by course (Bonus) |
| POST | /students | Add student |
| GET | /students/{id} | Get by ID |
| PUT | /students/{id} | Update student |
| DELETE | /students/{id} | Delete student |

Swagger UI: http://localhost:8000/docs
