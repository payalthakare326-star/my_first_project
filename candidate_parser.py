import re

def extract_details(text):
    details = {}

    # Email
    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    details["email"] = email[0] if email else "Not Found"

    # Phone
    phone = re.findall(r'\b\d{10}\b', text)
    details["phone"] = phone[0] if phone else "Not Found"

    # Name
    details["name"] = "Not Found"

    ignore = {
        "RESUME",
        "CURRICULUM VITAE",
        "CV",
        "CAREER OBJECTIVE",
        "OBJECTIVE",
        "PROFILE",
        "SUMMARY",
        "EDUCATION",
        "SKILLS",
        "PROJECTS",
        "EXPERIENCE"
    }

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    for line in lines:
        if line.upper() in ignore:
            continue

        if re.fullmatch(r"[A-Za-z ]{3,40}", line):
            details["name"] = line
            break

    return details