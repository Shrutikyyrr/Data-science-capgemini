"""
Section 3: Database Integration (SQLite + SQLAlchemy)
- Full CRUD with persistent SQLite DB
- Bonus: search by name keyword (?name=ali) and min_score filter
"""

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student API – Section 3 (DB Integration)")


@app.get("/students", response_model=List[schemas.StudentOut])
def get_students(
    course: Optional[str] = Query(None),
    name: Optional[str] = Query(None, description="Search: name contains keyword"),
    min_score: Optional[float] = Query(None, description="Filter: score >= value"),
    db: Session = Depends(get_db)
):
    q = db.query(models.Student)
    if course:
        q = q.filter(models.Student.course == course)
    if name:
        q = q.filter(models.Student.name.ilike(f"%{name}%"))   # case-insensitive
    if min_score is not None:
        q = q.filter(models.Student.score >= min_score)
    return q.all()


@app.post("/students", response_model=schemas.StudentOut, status_code=201)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/students/{id}", response_model=schemas.StudentOut)
def get_student(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.put("/students/{id}", response_model=schemas.StudentOut)
def update_student(id: int, updates: schemas.StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    for field, value in updates.model_dump(exclude_none=True).items():
        setattr(student, field, value)
    db.commit()
    db.refresh(student)
    return student


@app.delete("/students/{id}", status_code=204)
def delete_student(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
