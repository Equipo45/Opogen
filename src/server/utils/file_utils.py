from io import BytesIO, StringIO

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from utils.logger import logger

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


def load_file_auto_detect(uploaded_file) -> str:
    encodings = ['utf-8', 'latin-1', 'utf-16']

    for encoding in encodings:
        try:
            stringio = StringIO(uploaded_file.getvalue().decode(encoding))
            string_data = stringio.read()
            return string_data
        except UnicodeDecodeError:
            continue

    raise ValueError("Unable to decode the file with any of the specified encodings")
    
def write_to_txt(strings, file_name):
    try:
        with open(file_name, 'a') as file:
            file.write(strings + '\n')
        print("Las cadenas se han escrito en el archivo:", file_name)
    except Exception as e:
        print("Error al escribir en el archivo:", e)