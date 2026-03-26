"""Database initialization"""

from database.session import engine, SessionLocal, get_db
from models.base import Base

# Create all tables
Base.metadata.create_all(bind=engine)

__all__ = ["engine", "SessionLocal", "get_db", "Base"]
