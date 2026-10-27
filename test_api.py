import requests


def test_get_post_returns_expected_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=15
    )

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")

    data = response.json()

    assert isinstance(data, dict)

    assert data["id"] == 1
    assert isinstance(data["title"], str)
    assert data["title"] != ""

def test_get_nonexistent_post_returns_404():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/999999",
        timeout=15
    )

    assert response.status_code == 404

def test_create_post_returns_created_data():
    payload = {
        "title": "QA practice",
        "body": "Testing POST endpoint",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload,
        timeout=15
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert isinstance(data["id"], int)