from fastapi import FastAPI
import os

app = FastAPI(title="OrderFlow API", version="1.0.0")


@app.get("/health")
def health_check():
    db_status = "connected" if os.getenv("DATABASE_URL") else "disconnected"
    return {"status": "healthy", "database": db_status, "version": "1.0.0"}


@app.get("/api/v1/orders")
def get_orders():
    return [{"order_id": 101, "item": "Cloud Server", "status": "processed"}]
