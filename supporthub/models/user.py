"""User Model"""

from sqlalchemy import Column, Integer, String, Boolean
from models.base import BaseModel


class User(BaseModel):
    """User/Admin model"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    full_name = Column(String(255))
    role = Column(String(50))  # admin, moderator, analyst
    is_active = Column(Boolean, default=True)
    organization_id = Column(Integer)
