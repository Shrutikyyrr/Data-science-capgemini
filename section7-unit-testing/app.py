"""
The app being tested — same as Section 1 (in-memory, no DB needed for unit tests)
"""
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

students_db: dict = {}
counter_ref = [1]   # list so it's mutable inside functions


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=1, le=100)
    course: str = Field(..., min_length=1, max_length=100)


class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    age: Optional[int] = Field(None, ge=1, le=100)
    course: Optional[str] = Field(None, min_length=1, max_length=100)


class StudentOut(BaseModel):
    id: int
    name: str
    age: int
    course: str


@app.get("/students", response_model=List[StudentOut])
def get_students(course: Optional[str] = Query(None)):
    result = list(students_db.values())
    if course:
        result = [s for s in result if s["course"].lower() == course.lower()]
    return result


@app.post("/students", response_model=StudentOut, status_code=201)
def create_student(student: StudentCreate):
    new = {"id": counter_ref[0], **student.model_dump()}
    students_db[counter_ref[0]] = new
    counter_ref[0] += 1
    return new


@app.get("/students/{id}", response_model=StudentOut)
def get_student(id: int):
    if id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    return students_db[id]


@app.put("/students/{id}", response_model=StudentOut)
def update_student(id: int, updates: StudentUpdate):
    if id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    for field, value in updates.model_dump(exclude_none=True).items():
        students_db[id][field] = value
    return students_db[id]


@app.delete("/students/{id}", status_code=204)
def delete_student(id: int):
    if id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found")
    del students_db[id]
