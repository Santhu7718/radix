from app.parser.pdf_parser import read_pdf
from app.parser.docx_parser import read_docx

def extract_text(file_path):

    if file_path.endswith(".pdf"):
        return read_pdf(file_path)

    elif file_path.endswith(".docx"):
        return read_docx(file_path)

    raise Exception("Unsupported file format.")