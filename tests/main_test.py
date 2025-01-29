from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_health_check():
    response = client.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_request():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.text == "<span style='color:#ff0000;'>GETリクエスト!</span>"


def test_post_request():
    response = client.post("/hello")
    assert response.status_code == 200
    assert response.text == "<span style='color:#00bf00;'>POSTリクエスト!</span>"


def test_put_request():
    response = client.put("/hello")
    assert response.status_code == 200
    assert response.text == "<span style='color:#0000ff;'>PUTリクエスト!</span>"


def test_patch_request():
    response = client.patch("/hello")
    assert response.status_code == 200
    assert response.text == "<span style='color:#ff00ff;'>PATCHリクエスト!</span>"


def test_delete_request():
    response = client.delete("/hello")
    assert response.status_code == 200
    assert response.text == "<span style='color:#ff9900;'>DELETEリクエスト!</span>"
