"""
OrderFlow API - Enterprise DevSecOps & Production CI/CD Pipeline

This package contains the core FastAPI application and database utilities
for the OrderFlow microservice.
"""

from app.main import app
from app.database import get_db, get_engine

__version__ = "1.0.0"
__all__ = ["app", "get_db", "get_engine"]
