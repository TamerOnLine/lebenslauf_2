from sqlalchemy import Column, Integer, String, Text, Boolean
from config.database import Base

class ResumeSection(Base):
    __tablename__ = "resume_sections"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    order = Column(Integer, default=0)
    is_visible = Column(Boolean, default=True)
