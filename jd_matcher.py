def match_job_description(resume_skills, job_description):
    
    all_skills = [
        "Python",
        "SQL",
        "Flask",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "HTML",
        "CSS",
        "JavaScript",
        "MySQL",
        "Git",
        "Java",
        "C++",
        "Data Analysis",
        "TensorFlow",
        "Scikit-learn"
    ]

    jd = job_description.lower()

    jd_skills = []

    for skill in all_skills:
        if skill.lower() in jd:
            jd_skills.append(skill)

    matched = []

    for skill in jd_skills:
        if skill in resume_skills:
            matched.append(skill)

    missing = []

    for skill in jd_skills:
        if skill not in matched:
            missing.append(skill)

    if len(jd_skills) == 0:
        percentage = 0
    else:
        percentage = round((len(matched) / len(jd_skills)) * 100)

    return matched, missing, percentage