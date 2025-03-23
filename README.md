# AI Resume Screening & Candidate Ranking System  

## Overview  
This project is an **AI-powered resume screening system** that ranks resumes based on job descriptions using **Natural Language Processing (NLP)** and **Machine Learning (ML)**. It extracts key information from resumes and compares them with job requirements to assign a relevance score.  

## Features  
- Upload resumes in **PDF and TXT** formats  
- Compare resumes against a job description  
- Assign a **relevance score** to each resume  
- Uses **Sentence Transformers (BERT-based model)** for similarity scoring  
- Web interface built with **Streamlit**  
- Supports **multiple resume uploads**  

## Tech Stack  
- **Python**  
- **NLP**: SpaCy, NLTK  
- **Machine Learning**: Sentence Transformers  
- **Web Framework**: Streamlit  
- **Resume Parsing**: PyMuPDF (fitz)  

## File Structure  
```plaintext
resume-screening/
│── main.py            # Streamlit web app
│── backend.py         # NLP-based resume ranking logic
│── requirements.txt   # Required dependencies
│── README.md          # Project documentation
│── sample_resume.pdf  # Example resume for testing

