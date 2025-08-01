# 💼 Job Application Agent (GenAI Project)

This is an AI-powered assistant that helps job seekers instantly generate a full application kit — including optimized resume bullet points, a tailored cover letter, mock interview Q&A, ATS score analysis, and missing skill detection — using just their resume and a job description.

Built using **Python**, **Streamlit**, and **Groq’s LLaMA 3 API**.

---

## 🚀 Features

- 📄 **Resume Bullet Point Optimizer**  
  Rewrites your resume points to better align with the job description.

- 📨 **Cover Letter Generator**  
  Creates a personalized, professional cover letter.

- 🧠 **Interview Q&A Generator**  
  Predicts questions and suggests strong, resume-based answers.

- 📊 **ATS Match Score**  
  Compares your resume to the job description using keyword similarity.

- 📋 **Resume Health Check**  
  Evaluates formatting, content, and section completeness.

- 📉 **Skill Gap Analyzer**  
  Detects missing skills from the job description not found in your resume.

---

## 🧰 Tech Stack

- 🐍 Python  
- 🌐 Streamlit (Frontend UI)  
- 🔗 Groq API (LLaMA 3)  
- 🧠 LangChain (Optional for agent control logic)  
- 📊 Scikit-learn (for ATS scoring)  

---

## 📦 Setup Instructions

1.**Clone the repo**  
  
   git clone https://github.com/your-username/job-application-agent.git
   
   cd job-application-agent
   
2.Install dependencies
pip install -r requirements.txt

3.Add your API key to .env
GROQ_API_KEY=your_api_key_here

4.Run
streamlit run app.py
