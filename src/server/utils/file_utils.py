import PyPDF2
import docx
from fpdf import FPDF

from utils.str_utils import extract_title_from_path

def load_pdf(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return text

def load_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

def load_txt(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()

def load_string(input_string: str) -> str:
    return input_string

def write_to_txt(strings: str, file_name: str) -> None:
    try:
        with open(file_name, 'a') as file:
            file.write(strings + '\n')
        print("Las cadenas se han escrito en el archivo:", file_name)
    except Exception as e:
        print("Error al escribir en el archivo:", e)

def load_file_auto_detect(file_path: str) -> None:
    if file_path.endswith('.pdf'):
        return load_pdf(file_path)
    elif file_path.endswith('.docx'):
        return load_docx(file_path)
    elif file_path.endswith('.txt'):
        return load_txt(file_path)
    else:
        raise ValueError("Unsupported file format")
    
def txt_to_pdf(input_file: str, output_file: str, font_family='Arial', font_size=11) -> None:
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    pdf = FPDF()
    pdf.add_page()
    
    title = extract_title_from_path(input_file)
    pdf.set_title(title)
    
    pdf.set_font(font_family, size=font_size)
    pdf.write(h=font_size/2, txt=text)
    
    pdf.output(output_file)
