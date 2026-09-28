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
    return {"status": "healthy"}
    
