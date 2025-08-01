from backend.llm_client import call_llm

def generate_interview_qa(resume_text: str, jd_text: str) -> str:
    prompt = f"""
You are an expert interview coach.

Based on the resume and job description below, generate 5 interview questions likely to be asked for this role.
For each question, provide a sample answer using the candidate's experience from the resume.

Resume:
{resume_text}

Job Description:
{jd_text}

Format:
Q1: [Question]
A1: [Answer]

Q2: ...
Only include 5 Q&A pairs.
"""
    return call_llm(prompt)
    