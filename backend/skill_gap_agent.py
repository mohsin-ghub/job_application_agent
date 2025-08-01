import re

# A basic list of real skills (you can expand this)
KNOWN_SKILLS = {
    "python", "java", "c++", "javascript", "html", "css", "react", "nodejs",
    "fastapi", "flask", "django", "tensorflow", "pytorch", "scikit-learn",
    "sql", "mongodb", "postgresql", "docker", "kubernetes", "aws", "azure",
    "git", "linux", "pandas", "numpy", "excel", "powerbi", "matplotlib",
    "rest", "api", "oop", "nlp", "ml", "ai", "deep learning", "data analysis",
    "communication", "teamwork", "leadership"
}

def extract_keywords(text: str) -> set:
    words = re.findall(r"\b[a-zA-Z\-\+]{2,}\b", text.lower())
    return set(words)

def find_missing_skills(resume_text: str, jd_text: str) -> list:
    resume_words = extract_keywords(resume_text)
    jd_words = extract_keywords(jd_text)

    # Match only known skills
    jd_skills = {word for word in jd_words if word in KNOWN_SKILLS}
    resume_skills = {word for word in resume_words if word in KNOWN_SKILLS}

    # What's in JD but not in resume
    missing = jd_skills - resume_skills
    return sorted(missing)
