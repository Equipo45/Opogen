from typing import Dict, List
from llm.parsers import parsers
from llm.llm_service import get_opo_response
from utils.str_utils import search_test_letter
from utils.file_utils import write_to_txt, txt_to_pdf

WRITE_FILE_PATH = "src/opogen/response_file/Examen_Prueba_3.txt"
ENUM_LIST = ["A", "B", "C", "D", "E", "F"]
PARSE_PDF_PATH = "src/opogen/response_file/Examen_Prueba_3.pdf"

def _opo_json_response(chunks:List[str]) -> Dict[str, List]: 
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
    return all_responses


def write_chunk_to_pdf(chunks:List[str]) -> None:
    all_responses = _opo_json_response(chunks)
    for enum_index, response_index in enumerate(range(len(all_responses["questions"]))):
        write_to_txt(str(enum_index + 1) + ". "+ all_responses["questions"][response_index] + "\n", WRITE_FILE_PATH)

        for answer_index, answer in enumerate(range(len(all_responses["answers"][response_index]))):
            final_answer = all_responses["answers"][response_index][answer]
            if search_test_letter(final_answer):
                write_to_txt(final_answer, WRITE_FILE_PATH)
            else:
                write_to_txt(ENUM_LIST[answer_index] + ") " + final_answer, WRITE_FILE_PATH)
        write_to_txt("", WRITE_FILE_PATH)
    write_to_txt("***SOLUCIONES***", WRITE_FILE_PATH)
    for enum_index, response_index in enumerate(range(len(all_responses["correct_response"]))):
        response_number = f"Solución pregunta número {enum_index + 1}:"
        write_to_txt(response_number + " " + all_responses["correct_response"][response_index], WRITE_FILE_PATH)
    
    txt_to_pdf(WRITE_FILE_PATH, PARSE_PDF_PATH)