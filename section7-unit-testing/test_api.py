"""
Section 7: API Endpoint Tests
Uses fixtures from conftest.py
"""


def test_create_student(client):
    resp = client.post("/students", json={"name": "Alice", "age": 21, "course": "AI"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "Alice"
    assert data["age"] == 21
    assert data["course"] == "AI"
    assert "id" in data


def test_get_all_students_empty(client):
    resp = client.get("/students")
    assert resp.status_code == 200
    assert resp.json() == []


def test_get_all_students(client, sample_student):
    resp = client.get("/students")
    assert resp.status_code == 200
    assert len(resp.json()) == 1


def test_get_student_by_id(client, sample_student):
    sid = sample_student["id"]
    resp = client.get(f"/students/{sid}")
    assert resp.status_code == 200
    assert resp.json()["name"] == "Alice"


def test_get_student_not_found(client):
    resp = client.get("/students/9999")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Student not found"


def test_update_student(client, sample_student):
    sid = sample_student["id"]
    resp = client.put(f"/students/{sid}", json={"age": 30, "course": "ML"})
    assert resp.status_code == 200
    assert resp.json()["age"] == 30
    assert resp.json()["course"] == "ML"


def test_update_student_not_found(client):
    resp = client.put("/students/9999", json={"age": 25})
    assert resp.status_code == 404


def test_delete_student(client, sample_student):
    sid = sample_student["id"]
    del_resp = client.delete(f"/students/{sid}")
    assert del_resp.status_code == 204
    get_resp = client.get(f"/students/{sid}")
    assert get_resp.status_code == 404


def test_delete_student_not_found(client):
    resp = client.delete("/students/9999")
    assert resp.status_code == 404


def test_filter_by_course(client):
    client.post("/students", json={"name": "Alice", "age": 21, "course": "AI"})
    client.post("/students", json={"name": "Bob", "age": 22, "course": "ML"})
    resp = client.get("/students?course=AI")
    assert resp.status_code == 200
    assert all(s["course"] == "AI" for s in resp.json())
    assert len(resp.json()) == 1


def test_validation_invalid_age(client):
    resp = client.post("/students", json={"name": "X", "age": -1, "course": "AI"})
    assert resp.status_code == 422


def test_validation_empty_name(client):
    resp = client.post("/students", json={"name": "", "age": 20, "course": "AI"})
    assert resp.status_code == 422


def test_validation_missing_field(client):
    resp = client.post("/students", json={"name": "Alice", "age": 21})
    assert resp.status_code == 422
