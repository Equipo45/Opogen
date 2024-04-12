from utils.logger import logger

import PyPDF2
import docx
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


def load_pdf(file_path: str) -> str:
    with open(file_path, "rb") as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return text


def load_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)


def load_txt(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


def load_string(input_string: str) -> str:
    return input_string


def write_to_pdf(
    text: str,
    output_pdf: BytesIO,
    font_name: str = "Arial",
    font_size: int = 11,
) -> None:
    try:
        c = canvas.Canvas(output_pdf, pagesize=letter)
        pdfmetrics.registerFont(TTFont("Arial", "Arial.ttf"))
        c.setFont(font_name, font_size)
        c.drawString(100, 700, text)  # Adjust position as needed
        c.save()

        logger.info("Text has been written to the PDF")
    except Exception as e:
        logger.error("Error writing to PDF:", e)


def load_file_auto_detect(file_path: str) -> None:
    if file_path.endswith(".pdf"):
        return load_pdf(file_path)
    elif file_path.endswith(".docx"):
        return load_docx(file_path)
    elif file_path.endswith(".txt"):
        return load_txt(file_path)
    else:
        logger.error(f"A user uploaded an unsoported format {file_path.split('.')[-1]}")
        raise ValueError("Unsupported file format")
