"""Report Model"""

from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from models.base import BaseModel


class Report(BaseModel):
    """Report model for harassment/abuse incidents"""

    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    report_id = Column(String(50), unique=True, index=True)
    description = Column(Text)
    reporter_email_hash = Column(String(255))  # Anonymous but traceable
    abuse_type = Column(String(100))
    severity_score = Column(Float, default=0.0)
    severity_level = Column(String(50))  # Low, Medium, High, Critical
    location = Column(String(255))
    incident_date = Column(DateTime)
    status = Column(String(50), default="pending")  # pending, under_review, resolved
    organization_id = Column(Integer)
