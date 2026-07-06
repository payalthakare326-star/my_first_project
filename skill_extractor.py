def extract_skills(text):
    
    skills = [
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

    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))