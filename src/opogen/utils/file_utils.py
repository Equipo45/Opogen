import PyPDF2
import docx

def load_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return text

def load_docx(file_path):
    doc = docx.Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

def load_txt(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def load_string(input_string):
    return input_string

def write_to_txt(strings, file_name):
    try:
        with open(file_name, 'a') as file:
            file.write(strings + '\n')
        print("Las cadenas se han escrito en el archivo:", file_name)
    except Exception as e:
        print("Error al escribir en el archivo:", e)

def load_file_auto_detect(file_path):
    if file_path.endswith('.pdf'):
        return load_pdf(file_path)
    elif file_path.endswith('.docx'):
        return load_docx(file_path)
    elif file_path.endswith('.txt'):
        return load_txt(file_path)
    else:
        raise ValueError("Unsupported file format")