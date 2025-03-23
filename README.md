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
```



Installation & Setup
1. Clone the Repository
sh
Copy
Edit
git clone https://github.com/username/resume-screening.git
cd resume-screening
2. Create a Virtual Environment (Optional but Recommended)
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
3. Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4. Download NLP Model
sh
Copy
Edit
python -m spacy download en_core_web_sm
5. Run the Application
sh
Copy
Edit
streamlit run main.py
Usage
1. Upload Resumes & Enter Job Description
Select and upload multiple resumes

Input the job description

Click "Rank Resumes" to get scores

2. View Results
The app will display resumes ranked by relevance

Higher scores indicate a better match

Example Job Description
plaintext
Copy
Edit
Job Title: AI/ML Engineer  
Company: ABC Tech Solutions  

Responsibilities:  
- Develop AI-based applications using Python, NLP, and ML  
- Work with TensorFlow, SpaCy, and Scikit-learn for AI model training  
- Process unstructured data for AI-driven insights  
- Collaborate with cross-functional teams  

Requirements:  
- Bachelor’s in Computer Science or related field  
- Experience with NLP and AI-driven applications  
- Proficiency in Python, SQL, and web frameworks  
Deployment
1. Push Code to GitHub
sh
Copy
Edit
git add .
git commit -m "Initial commit"
git push origin main
2. Deploy on Streamlit Cloud
Go to Streamlit Community Cloud

Click "New app" → Select GitHub repository

Set main.py as the entry point

Deploy & share the link

Requirements.txt
plaintext
Copy
Edit
streamlit
sentence-transformers
spacy
nltk
pymupdf
Future Enhancements
Use BERT/GPT for better semantic matching

Add multi-language support

Improve data visualization with interactive dashboards

Implement custom deep learning models

License
This project is open-source and free to use.'''



