from pydantic import BaseModel, Field
from typing import Optional


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=1, le=100)
    course: str = Field(..., min_length=1, max_length=100)
    score: Optional[float] = Field(None, ge=0, le=100)


class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    age: Optional[int] = Field(None, ge=1, le=100)
    course: Optional[str] = Field(None, min_length=1, max_length=100)
    score: Optional[float] = Field(None, ge=0, le=100)


class StudentOut(BaseModel):
    id: int
    name: str
    age: int
    course: str
    score: Optional[float] = None

    class Config:
        from_attributes = True
