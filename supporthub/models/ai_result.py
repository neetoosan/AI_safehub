"""AI Analysis Result Model"""

from sqlalchemy import Column, Integer, String, Float, JSON, Text
from models.base import BaseModel


class AIResult(BaseModel):
    """AI analysis results for reports"""

    __tablename__ = "ai_results"

    id = Column(Integer, primary_key=True)
    report_id = Column(Integer)
    classification = Column(JSON)  # {abuse_type: confidence}
    severity_score = Column(Float)
    severity_factors = Column(JSON)  # List of contributing factors
    pattern_matches = Column(JSON)  # Linked report IDs
    confidence_score = Column(Float)
    explainability = Column(Text)  # Why the AI made this decision
