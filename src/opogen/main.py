from utils.file_utils import load_file_auto_detect

if __name__ == "__main__":
    file_path = "src/opogen/read_files/FASES DEL PROCEDIMIENTO ADMINISTRATIVO.docx"
    text = load_file_auto_detect(file_path)
    print(text)