from flask import Flask, render_template, request
from candidate_parser import extract_details
from skill_extractor import extract_skills
from resume_score import calculate_score
from jd_matcher import match_job_description

import os
import pdfplumber
from docx import Document

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    files = request.files.getlist("resume")
    job_description = request.form.get("job_description", "")

    results = []

    for file in files:

        if file.filename == "":
            continue

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        text = ""

        # Read PDF
        if file.filename.lower().endswith(".pdf"):
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

        # Read DOCX
        elif file.filename.lower().endswith(".docx"):
            doc = Document(filepath)
            for para in doc.paragraphs:
                text += para.text + "\n"

        # Extract email and phone
        details = extract_details(text)

        # Candidate name from filename
        candidate_name = os.path.splitext(file.filename)[0]
        candidate_name = candidate_name.replace("_Resume", "")
        candidate_name = candidate_name.replace("_resume", "")
        candidate_name = candidate_name.replace("-", " ")
        candidate_name = candidate_name.replace("_", " ")

        details["name"] = candidate_name

        # Extract resume skills
        skills = extract_skills(text)

        # Resume Score
        score = calculate_score(skills)

        # JD Match
        matched, missing, match_percentage = match_job_description(
            skills,
            job_description
        )

        # Debug (optional)
        print("===================================")
        print("Candidate:", details["name"])
        print("Resume Skills:", skills)
        print("Matched:", matched)
        print("Missing:", missing)
        print("JD Match:", match_percentage)
        print("===================================")

        results.append({
            "filename": file.filename,
            "name": details["name"],
            "email": details["email"],
            "phone": details["phone"],
            "skills": skills,
            "score": score,
            "matched": matched,
            "missing": missing,
            "match_percentage": match_percentage
        })

    # Sort by Resume Score
    results.sort(key=lambda x: x["score"], reverse=True)

    return render_template("result.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)