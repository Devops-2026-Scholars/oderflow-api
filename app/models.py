from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""


class Order(Base):
    """Database model representing an order."""

    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    item: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="pending",
        server_default="pending",
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
