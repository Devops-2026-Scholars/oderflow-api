import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://devuser:devpassword@localhost:5432/orderdb",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_db() -> None:
    """Create database tables if they do not already exist."""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Provide a database session to callers."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_engine():
    """Return the SQLAlchemy engine instance."""
    return engine
