from backend.llm_client import call_llm

def generate_cover_letter(resume_text: str, jd_text: str) -> str:
    prompt = f"""
You are a professional career coach and cover letter expert.

Using the resume and job description below, write a compelling, personalized cover letter:
- Address the hiring team (e.g., "Dear Hiring Manager")
- Mention the role and company
- Highlight 2–3 achievements relevant to the JD
- Keep the tone confident and professional
- Keep the length to 3–4 concise paragraphs

Resume:
{resume_text}

Job Description:
{jd_text}

Return only the cover letter, no headings or notes.
"""
    return call_llm(prompt)
