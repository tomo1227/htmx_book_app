import re

import pytest
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


@pytest.mark.parametrize(
    "method, expected_status, expected_text",
    [
        ("get", 200, "<span style='color:#ff0000;'>GETリクエスト!</span>"),
        ("post", 200, "<span style='color:#00bf00;'>POSTリクエスト!</span>"),
        ("put", 200, "<span style='color:#0000ff;'>PUTリクエスト!</span>"),
        ("patch", 200, "<span style='color:#ff00ff;'>PATCHリクエスト!</span>"),
        ("delete", 200, "<span style='color:#ff9900;'>DELETEリクエスト!</span>"),
    ],
)
def test_hello(subtests, method, expected_status, expected_text):
    with subtests.test(msg=f"Testing {method.upper()} request"):
        response = getattr(client, method)("/hello")
        assert response.status_code == expected_status
        assert expected_text == response.text


def test_yahoo():
    expected_text = "<span style='color:#ff0000;'>やっほー!</span>"
    response = client.get("/yahoo")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert expected_text == response.text


def test_generate_random_number():
    response = client.get("/random")
    assert response.status_code == 200  # ステータスコードが200であること

    content = response.text
    assert content.startswith("<span style='color:#ff0000;'")
    assert content.endswith("</span>")

    match = re.search(r">(\d+)</span>", content)
    assert match is not None
    number = int(match.group(1))
    assert 0 <= number < 10


def test_load_polling():
    response = client.get("/random_polling")
    assert response.status_code == 200

    content = response.text
    assert content.startswith("<p style='color:#ff0000;'")
    assert "hx-get='/random_polling'" in content
    assert "hx-trigger='load delay:1s'" in content
    assert content.endswith("</p>")

    match = re.search(r">(\d+)</p>", content)
    assert match is not None
    number = int(match.group(1))
    assert 0 <= number < 10
