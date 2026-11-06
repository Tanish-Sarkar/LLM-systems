from fastapi.testclient import TestClient
from fastapi_starter.server import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "welcome to the world server"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Good Condition",
        "status": 200
    }


def test_query_valid():
    response = client.post(
        "/query",
        json={"query": "Explain RAG"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "query": "Explain RAG",
        "message": "query recieved"
    }


def test_query_missing():
    response = client.post("/query", json={})

    assert response.status_code == 422


def test_query_empty():
    response = client.post(
        "/query",
        json={"query": ""}
    )

    assert response.status_code == 422


def test_query_too_long():
    response = client.post(
        "/query",
        json={"query": "a" * 301}
    )

    assert response.status_code == 422
