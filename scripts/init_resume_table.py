# scripts/init_resume_table.py

from config.database import engine
from sqlalchemy.orm import declarative_base
from models.resume_section import ResumeSection

Base = declarative_base()

def init_resume_table():
    print("Initializing resume_sections table...")
    ResumeSection.__table__.create(bind=engine, checkfirst=True)
    print("✅ resume_sections table created (if not exists).")

if __name__ == "__main__":
    init_resume_table()
