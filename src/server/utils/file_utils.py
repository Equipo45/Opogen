import os
from io import BytesIO

from reportlab.lib.pagesizes import letter

from fpdf import FPDF
import PyPDF2
import docx

script_dir = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(script_dir, "logs", "download_files")

def load_string(input_string: str) -> str:
    return input_string

def load_file_auto_detect(uploaded_file) -> str:
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "pdf":
        text = read_pdf(uploaded_file)
    elif file_type == "docx":
        text = read_docx(uploaded_file)
    elif file_type == "txt":
        text = read_txt(uploaded_file)
    else:
        return "Unsupported file type! Please upload a PDF, DOCX, or TXT file."
    
    return text
    
def _get_filename_directoryname(file_name):
    file_path =  os.path.join(LOG_FILE_PATH, (file_name + ".txt"))
    directory_path = os.path.dirname(file_path)
    
    return file_path, directory_path
    
def write_to_txt(strings, file_name):
    try:
        file_path, directory = _get_filename_directoryname(file_name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(file_path, 'a') as file:
            file.write(strings + '\n')
        print("Strings have been written to the file:", file_name)
    except Exception as e:
        print("Error al escribir en el archivo:", e)
        
def txt_to_pdf_with_font(txt_file_path, font_name="Arial", font_size=12, page_format = "---"):
    try:
        file_path, _ = _get_filename_directoryname(txt_file_path)
        with open(file_path, 'r') as file:
            text = file.read()

        pdf = FPDF()
        for segment in text.split(page_format):
            pdf.add_page()
            pdf.set_font(font_name, size=font_size)
            pdf.multi_cell(0, 10, segment)

        return pdf.output(dest='S').encode('latin1')
    except Exception as e:
        raise Exception("Error converting txt to pdf:", e)

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

def read_txt(file):
    return file.getvalue().decode("utf-8")


def remove_final_extension(filename):
    base, ext = os.path.splitext(filename)
    if ext:
        return base
    else:
        return filename