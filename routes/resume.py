from flask import Blueprint, render_template
from models.resume_section import ResumeSection
from config.database import SessionLocal

resume_bp = Blueprint("resume", __name__)

@resume_bp.route("/resume")
def resume_page():
    db = SessionLocal()
    sections = db.query(ResumeSection).order_by(ResumeSection.order).all()
    return render_template("resume.html", sections=sections)
