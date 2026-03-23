"""Minimal app for CI/CD demo — same as Section 1"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()
students_db: dict = {}
counter_ref = [1]


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=1, le=100)
    course: str = Field(..., min_length=1, max_length=100)


class StudentOut(BaseModel):
    id: int
    name: str
    age: int
    course: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/students", response_model=List[StudentOut])
def get_students():
    return list(students_db.values())


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
