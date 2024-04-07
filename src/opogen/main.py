from utils.file_utils import load_file_auto_detect
from utils.str_utils import extract_articles, delete_word_regex, delete_bloq
from llm.llm_service import get_opo_response, init_config
from config import config
from llm.parsers import parsers

def main():
    init_config(config["OPEN_AI_KEY"])

    file_path = "src/opogen/read_files/FASES DEL PROCEDIMIENTO ADMINISTRATIVO.docx"
    text = load_file_auto_detect(file_path)
    formated_text = delete_bloq(text)
    formated_text = delete_word_regex(formated_text, "Subir")
    chunks = extract_articles(formated_text)

    question = []
    answers = []
    correct_response = []

    response = get_opo_response(chunks[15].strip(), parsers["three_answers"])

    question.append(response.question)
    answers.append(response.response)
    correct_response.append(response.correct_response)

    print(question, answers, correct_response)

if __name__ == "__main__":
    main()