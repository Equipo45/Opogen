import os
from io import BytesIO, StringIO

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

from utils.logger import logger

script_dir = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(script_dir, "logs", "download_files")

def load_string(input_string: str) -> str:
    return input_string

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
        
def txt_to_pdf_with_font(txt_file_path, font_name='Arial', font_size=12, pdf_file_path=None):
    try:
        file_path, _ = _get_filename_directoryname(txt_file_path)
        with open(file_path, 'r') as file:
            text = file.read()
            
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)

        style = getSampleStyleSheet()['Normal']
        style.fontName = font_name
        style.fontSize = font_size

        content = [Paragraph(text, style)]
        doc.build(content)
        pdf_bytes = buffer.getvalue()

        if pdf_file_path:
            with open(pdf_file_path, 'wb') as pdf_file:
                pdf_file.write(pdf_bytes)

        return pdf_bytes
    except Exception as e:
        print("Error converting txt to pdf:", e)
        return None
        
def remove_final_extension(filename):
    base, ext = os.path.splitext(filename)
    if ext:
        return base
    else:
        return filename