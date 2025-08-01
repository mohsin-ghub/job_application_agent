import streamlit as st
from backend.controller_agent import process_application

st.set_page_config(page_title="Job Application Agent", layout="centered")

st.title("💼 Job Application Agent")
st.write("Upload your resume and paste a job description — get tailored bullet points, a custom cover letter, and interview Q&A.")

# Upload Resume
uploaded_resume = st.file_uploader("📄 Upload Resume", type=["pdf", "docx", "txt"])

# Paste JD
job_description = st.text_area("📌 Paste the Job Description here", height=200)

# Submit
if st.button("🚀 Generate Application Kit"):
    if not uploaded_resume or not job_description.strip():
        st.warning("Please upload a resume and paste a job description.")
    else:
        with st.spinner("Generating application kit using AI..."):
            try:
                result = process_application(uploaded_resume, job_description)

                # Output Results
                st.success("✅ Application kit generated!")

                st.subheader("📋 Resume ATS Health Check")
                st.progress(min(result["ats_health_score"] / 100, 1.0))
                st.markdown(f"**Score:** `{result['ats_health_score']}%`")

                for line in result["ats_health_feedback"]:
                    st.markdown(f"🔹 {line}")

                st.subheader("📉 Missing Skills (Compared to Job Description)")
                if result["missing_skills"]:
                    st.markdown("The following skills or keywords are missing from your resume:")
                    st.markdown(", ".join([f"❌ `{skill}`" for skill in result["missing_skills"]]))
                else:
                    st.success("✅ No major skills missing from your resume!")


                st.subheader("📝 Optimized Resume Points")
                for line in result["resume"].split("•"):
                    if line.strip():
                        st.markdown(f"• {line.strip()}")

                st.subheader("📨 Cover Letter")
                st.markdown(result["cover_letter"])

                st.subheader("🧠 Interview Q&A")
                st.markdown(result["interview"])


            except Exception as e:
                st.error(f"❌ Something went wrong: {str(e)}")
