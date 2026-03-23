"""
Pytest fixtures shared across all test files in Section 7.
"""
import pytest
from fastapi.testclient import TestClient
from app import app, students_db, counter_ref


@pytest.fixture(autouse=True)
def clear_db():
    """Reset in-memory DB before each test — ensures test isolation."""
    students_db.clear()
    counter_ref[0] = 1
    yield
    students_db.clear()
    counter_ref[0] = 1


@pytest.fixture
def client():
    """FastAPI test client fixture."""
    return TestClient(app)


@pytest.fixture
def sample_student(client):
    """Creates one student and returns the response JSON."""
    resp = client.post("/students", json={"name": "Alice", "age": 21, "course": "AI"})
    return resp.json()
