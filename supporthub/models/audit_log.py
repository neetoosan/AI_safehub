"""Audit Log Model"""

from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from models.base import BaseModel


class AuditLog(BaseModel):
    """Audit trail for all system actions"""

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action = Column(String(255))
    resource_type = Column(String(100))  # report, user, etc
    resource_id = Column(Integer)
    changes = Column(Text)  # JSON of what changed
    timestamp = Column(DateTime, default=datetime.utcnow)
