"""Tests that run automatically via GitHub Actions CI"""
import pytest
from fastapi.testclient import TestClient
from app import app, students_db, counter_ref


@pytest.fixture(autouse=True)
def reset():
    students_db.clear()
    counter_ref[0] = 1
    yield


@pytest.fixture
def client():
    return TestClient(app)


def test_health(client):
    assert client.get("/health").status_code == 200


def test_create_student(client):
    resp = client.post("/students", json={"name": "Alice", "age": 21, "course": "AI"})
    assert resp.status_code == 201
    assert resp.json()["name"] == "Alice"


def test_get_students(client):
    client.post("/students", json={"name": "Bob", "age": 22, "course": "ML"})
    resp = client.get("/students")
    assert resp.status_code == 200
    assert len(resp.json()) == 1


def test_get_student_not_found(client):
    assert client.get("/students/9999").status_code == 404


def test_validation_error(client):
    resp = client.post("/students", json={"name": "", "age": -1, "course": ""})
    assert resp.status_code == 422
