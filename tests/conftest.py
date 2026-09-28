import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="session")
def database_url():
    """Provides the PostgreSQL database URL from the test environment."""
    return os.getenv("DATABASE_URL", "postgresql://devuser:devpassword@localhost:5432/orderdb")

@pytest.fixture(scope="module")
def client():
    """Provides a reusable FastAPI TestClient instance."""
    with TestClient(app) as c:
        yield c
