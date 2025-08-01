from backend.resume_parser import extract_text_from_file
from backend.resume_agent import generate_resume_points
from backend.cover_letter_agent import generate_cover_letter
from backend.interview_agent import generate_interview_qa
from backend.ats_score import calculate_ats_score
from backend.ats_resume_health import evaluate_resume_health
from backend.skill_gap_agent import find_missing_skills

def process_application(resume_file, job_description: str) -> dict:
    # 1. Extract plain text from the uploaded resume
    resume_text = extract_text_from_file(resume_file)

    # 2. Core AI Agents
    resume_output = generate_resume_points(resume_text, job_description)
    cover_letter_output = generate_cover_letter(resume_text, job_description)
    interview_output = generate_interview_qa(resume_text, job_description)

    # 3. ATS Score (Resume vs Job Description)
    jd_score = calculate_ats_score(resume_text, job_description)

    # 4. General Resume Health Score (JD-independent)
    resume_health = evaluate_resume_health(resume_text)

    # 5. Skill Gap Analysis
    missing_skills = find_missing_skills(resume_text, job_description)

    # 6. Return everything
    return {
        "resume": resume_output,
        "cover_letter": cover_letter_output,
        "interview": interview_output,
        "ats_score": jd_score,
        "ats_health_score": resume_health["ats_health_score"],
        "ats_health_feedback": resume_health["feedback"],
        "missing_skills": missing_skills
    }
