from fastapi.testclient import TestClient

from todo import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert 200 == response.status_code
    assert "text/html" in response.headers["content-type"]


def test_add_task():
    response = client.post("/add", data={"task": "Test Task"})
    assert 200 == response.status_code
    assert "Test Task" in response.text


def test_delete_nonexistent_task():
    response = client.delete("/delete", params={"task": "Nonexistent Task"})
    assert 204 == response.status_code
