import re

def evaluate_resume_health(resume_text: str) -> dict:
    score = 0
    feedback = []

    # 1. Standard sections
    if any(word in resume_text.lower() for word in ["experience", "education", "skills", "projects"]):
        score += 1
    else:
        feedback.append("Missing standard sections like 'Experience' or 'Skills'.")

    # 2. Contact info
    if re.search(r"\b[\w.-]+@[\w.-]+\.\w+\b", resume_text):
        score += 1
    else:
        feedback.append("Email is missing or not found.")

    # 3. Resume too short or too long
    word_count = len(resume_text.split())
    if 300 <= word_count <= 800:
        score += 1
    else:
        feedback.append("Resume might be too short or too long.")

    # Final score
    ats_health_score = round((score / 3) * 100)

    # Cap feedback to top 2 items
    if not feedback:
        feedback = ["Looks good! Your resume meets basic ATS guidelines."]

    return {
        "ats_health_score": ats_health_score,
        "feedback": feedback[:2]
    }
