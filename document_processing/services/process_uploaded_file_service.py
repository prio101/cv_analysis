import requests
import magic
import pytesseract
from pdf2image import convert_from_path
from docx import Document

class ProcessUploadedFileService:
    """Service class to process the uploaded file."""
    def __init__(self):
        self.extracted_text = ""

    def run(self, file_path: str):
        """Method to process the uploaded file."""

        response = requests.get(file_path)
        file_content = response.content
        mime = magic.Magic(mime=True)
        file_type = mime.from_buffer(file_content)

        if 'pdf' in file_type:
            self.extract_text_from_pdf(file_content)
        elif 'word' in file_type:
            self.extract_text_from_docx(file_content)

        return self.extracted_text

    def extract_text_from_pdf(self, pdf_content: bytes):
        """Extract text from a PDF using Tesseract OCR."""
        with open("temp.pdf", "wb") as f:
            f.write(pdf_content)
        images = convert_from_path("temp.pdf")  # Convert PDF pages to images
        text = ""

        for img in images:
            text += pytesseract.image_to_string(img) + "\n\n"

        self.extracted_text = text.strip()

    def extract_text_from_docx(self, docx_content: bytes):
        """Extract text from a .docx file."""
        with open("temp.docx", "wb") as f:
            f.write(docx_content)
        doc = Document("temp.docx")
        self.extracted_text = "\n".join([para.text for para in doc.paragraphs]).strip()
