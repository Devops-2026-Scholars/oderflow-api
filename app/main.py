import os
from fastapi import FastAPI
from app.database import init_db

app = FastAPI(title="OrderFlow API", version="1.0.0")


@app.on_event("startup")
def startup_event():
    """Initialize database on startup."""
    init_db()


@app.get("/")
def read_root():
    """Root endpoint."""
    return {"message": "OrderFlow API is running"}


@app.get("/health")
def health_check():
    """Health check endpoint."""
    db_status = "connected" if os.getenv("DATABASE_URL") else "disconnected"
    return {
        "status": "healthy",
        "database": db_status,
        "version": "1.0.0"
    }


@app.get("/api/v1/orders")
def get_orders():
    """Get all orders."""
    return [
        {
            "order_id": 101,
            "item": "Cloud Server",
            "status": "processed",
        }
    ]
