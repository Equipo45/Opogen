from utils.file_utils import load_file_auto_detect, write_to_txt, txt_to_pdf
from utils.str_utils import extract_articles, delete_word_regex, delete_bloq, search_test_letter
from llm.llm_service import get_opo_response, init_config
from config import config
from llm.parsers import parsers

def main():
    init_config(config["OPEN_AI_KEY"])
    ENUM_LIST = ["A", "B", "C", "D", "E", "F"]

    read_file_path = "src/opogen/read_files/OBJETO Y AMBITO DE APLICACION DE LA LEY 31-1995 DEL 8 DE NOVIEMBRE.docx"
    write_file_path = "src/opogen/response_file/Examen_Prueba_3.txt"
    parse_pdf_path = "src/opogen/response_file/Examen_Prueba_3.pdf"

    text = load_file_auto_detect(read_file_path)
    formated_text = delete_bloq(text)
    formated_text = delete_word_regex(formated_text, "Subir")
    chunks = extract_articles(formated_text)
    all_responses = {
        "questions": [],
        "answers": [],
        "correct_response": []
    }

    for chunk in chunks:
        try: 
            response = get_opo_response(chunk.strip(), parsers["three_answers"], prompt_version = 1.2, model="gpt-4-turbo-preview")
            all_responses["questions"].append(response.question)
            all_responses["answers"].append(response.response)
            all_responses["correct_response"].append(response.correct_response)
        except Exception as e:
            print(e)
            continue
        
    for enum_index, response_index in enumerate(range(len(all_responses["questions"]))):
        write_to_txt(str(enum_index + 1) + ". "+ all_responses["questions"][response_index] + "\n", write_file_path)

        for answer_index, answer in enumerate(range(len(all_responses["answers"][response_index]))):
            final_answer = all_responses["answers"][response_index][answer]
            if search_test_letter(final_answer):
                write_to_txt(final_answer, write_file_path)
            else:
                write_to_txt(ENUM_LIST[answer_index] + ") " + final_answer, write_file_path)
        write_to_txt("", write_file_path)
    write_to_txt("***SOLUCIONES***", write_file_path)
    for enum_index, response_index in enumerate(range(len(all_responses["correct_response"]))):
        response_number = f"Solución pregunta número {enum_index + 1}:"
        write_to_txt(response_number + " " + all_responses["correct_response"][response_index], write_file_path)
        
    txt_to_pdf(write_file_path, parse_pdf_path)
    
if __name__ == "__main__":
    main()