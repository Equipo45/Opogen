import PyPDF2

def load_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return text

def load_txt(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def load_string(input_string):
    return input_string

