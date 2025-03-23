import spacy
import fitz  # PyMuPDF for PDF extraction
from sentence_transformers import SentenceTransformer, util

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Load Sentence Transformer model for similarity scoring
model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_text_from_pdf(pdf_file):
    """Extract text from an uploaded PDF file."""
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text("text")
    return text


def preprocess_text(text):
    """Clean and preprocess text using NLP."""
    doc = nlp(text.lower())  # Convert text to lowercase
    return " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])


def compute_similarity(job_desc, resume_text):
    """Compute similarity score between job description and resume."""
    embeddings = model.encode([job_desc, resume_text], convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    return similarity.item()  # Convert tensor to float


def rank_resumes(job_desc, resumes):
    """Rank resumes based on similarity to job description."""
    results = []
    job_desc_cleaned = preprocess_text(job_desc)

    for resume_file in resumes:
        resume_text = extract_text_from_pdf(resume_file)  # Extract text from PDF
        resume_cleaned = preprocess_text(resume_text)

        score = compute_similarity(job_desc_cleaned, resume_cleaned)

        # Append (resume filename, score) as a tuple
        results.append((resume_file.name, score))

    return results  # Return a list of tuples






   


