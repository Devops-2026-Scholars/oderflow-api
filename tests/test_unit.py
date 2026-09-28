from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check_without_database(client):  # ← Add client parameter
    response = client.get("/health")
    ...


def test_health_check_without_database():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "database": "disconnected",
        "version": "1.0.0",
    }


def test_health_check_with_database(monkeypatch):
    monkeypatch.setenv(
        "DATABASE_URL",
        "postgresql://devuser:devpassword@localhost:5432/orderdb",
    )

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "database": "connected",
        "version": "1.0.0",
    }


def test_get_orders():
    response = client.get("/api/v1/orders")

    assert response.status_code == 200
    assert response.json() == [
        {
            "order_id": 101,
            "item": "Cloud Server",
            "status": "processed",
        }
    ]
