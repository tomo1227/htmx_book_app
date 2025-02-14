import json

from fastapi.testclient import TestClient

from chat import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_websocket_chatroom():
    with client.websocket_connect("/chatroom") as websocket:
        websocket.send_text(json.dumps({"name": "TestUser", "message": "Hello, World!"}))
        response = websocket.receive_text()
        assert "TestUser" in response
        assert "Hello, World!" in response
