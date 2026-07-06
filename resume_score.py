def calculate_score(skills):
    
    required_skills = [
        "Python",
        "SQL",
        "Flask",
        "HTML",
        "CSS",
        "MySQL",
        "Data Analysis",
        "Machine Learning",
        "TensorFlow",
        "Git"
    ]

    score = 0

    for skill in skills:
        if skill in required_skills:
            score += 10

    if score > 100:
        score = 100

    return score