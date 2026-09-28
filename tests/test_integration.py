import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from app.database import get_engine
from app.main import app


client = TestClient(app)


@pytest.fixture
def test_health_endpoint_with_postgresql(client, database_url):  # ← Add client parameter
    response = client.get("/health")
    ...


def database_url():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        pytest.fail("DATABASE_URL must be configured for integration tests")

    return database_url


def test_postgresql_connection(database_url):
    engine = get_engine()

    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.scalar() == 1
    finally:
        engine.dispose()


def test_health_endpoint_with_postgresql(database_url):
    response = client.get("/health")

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["status"] == "healthy"
    assert response_data["database"] == "connected"
    assert response_data["version"] == "1.0.0"


def test_orders_endpoint_integration(database_url):
    response = client.get("/api/v1/orders")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["order_id"] == 101
