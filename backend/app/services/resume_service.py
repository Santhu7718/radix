from app.parser.pdf_parser import read_pdf
from app.parser.docx_parser import read_docx

from app.ai.resume_extractor import extract_resume_information


def analyze_resume(file_path):
    """
    Extract text from the uploaded resume
    and analyze it using Gemini.
    """

    if file_path.lower().endswith(".pdf"):

        text = read_pdf(file_path)

    elif file_path.lower().endswith(".docx"):

        text = read_docx(file_path)

    else:

        raise Exception("Unsupported file format")

    return extract_resume_information(text)