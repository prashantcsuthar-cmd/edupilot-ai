import pdfplumber
from pypdf import PdfReader

def extract_text_from_pdf(pdf_file_path: str) -> str:
    """
    Extracts text cleanly from a PDF file path or file-like object.
    Uses pdfplumber first, falling back to pypdf if needed.
    """
    text = ""
    try:
        with pdfplumber.open(pdf_file_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except Exception as e:
        print(f"pdfplumber encountered an issue, trying pypdf fallback: {e}")
        try:
            reader = PdfReader(pdf_file_path)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
        except Exception as fallback_e:
            print(f"Failed to extract text from PDF: {fallback_e}")
            return ""
            
    return text.strip()