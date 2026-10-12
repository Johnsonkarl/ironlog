
from api import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_calculate():
    client = app.test_client()

    response = client.post("/calculate", json={
        "weight": 225,
        "reps": 5
    })

    assert response.status_code == 200
    assert response.json["estimated_1rm"] == 262.5


def test_invalid_reps():
    client = app.test_client()

    response = client.post("/calculate", json={
        "weight": 225,
        "reps": -5
    })

    assert response.status_code == 400


def test_homepage():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"IronLog" in response.data
