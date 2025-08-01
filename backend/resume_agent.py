from backend.llm_client import call_llm

def generate_resume_points(resume_text: str, jd_text: str) -> str:
    prompt = f"""
You are an expert resume writer.

Rewrite the key resume bullet points based on the job description below:
- Write **each point on a new line**, starting with the bullet symbol "•"
- Return only the **final improved bullet points** (4–6)
- Do **not** write them in a paragraph
- Do not add any heading or explanation

Resume:
{resume_text}

Job Description:
{jd_text}

Example format:
• Led cross-functional team for ML product launch  
• Built scalable backend services with FastAPI and PostgreSQL

Now, return your response in the same format.
"""
    return call_llm(prompt)
