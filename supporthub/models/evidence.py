"""Evidence Model"""

from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey
from models.base import BaseModel


class Evidence(BaseModel):
    """Evidence/Attachments for reports"""

    __tablename__ = "evidence"

    id = Column(Integer, primary_key=True)
    report_id = Column(Integer, ForeignKey("reports.id"))
    file_name = Column(String(255))
    file_type = Column(String(50))  # image, audio, document
    file_data = Column(LargeBinary)
    file_hash = Column(String(255))  # For duplicate detection
    file_size = Column(Integer)
