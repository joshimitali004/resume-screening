import streamlit as st
from backend import rank_resumes

st.title("AI Resume Screening & Ranking System")

st.subheader("Job Description")
job_desc = st.text_area("Enter job description", "")

st.subheader("Upload Resumes (PDF only)")
uploaded_files = st.file_uploader("Choose PDF resumes", type=["pdf"], accept_multiple_files=True)

if st.button("Rank Resumes"):
    if not job_desc or not uploaded_files:
        st.warning("Please enter a job description and upload resumes.")
    else:
        results = rank_resumes(job_desc, uploaded_files)

        st.subheader("Ranked Resumes")
        for i, (resume_name, score) in enumerate(results, 1):
            st.write(f"{i}. {resume_name}: **Score - {score:.2f}**")





