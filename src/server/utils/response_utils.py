from io import BytesIO
from typing import Dict, List

from _globals import ENUM_LIST
from llm.llm_service import get_opo_response
from llm.parsers import parsers
from utils.file_utils import (load_file_auto_detect, write_to_txt)
from utils.str_utils import (delete_bloq, delete_word_regex, extract_articles,
                             search_test_letter)


def _opo_json_response(chunks: List[str]) -> Dict[str, List]:
    all_responses = {"questions": [], "answers": [], "correct_response": []}

    for chunk in chunks:
        try:
            response = get_opo_response(
                chunk.strip(),
                parsers["three_answers"],
                prompt_version=1.2,
                model="gpt-4-turbo-preview",
            )
            all_responses["questions"].append(response.question)
            all_responses["answers"].append(response.response)
            all_responses["correct_response"].append(response.correct_response)
        except Exception as e:
            print(e)
            continue
    return all_responses


def write_chunk_return_pdf(chunks: List[str]) -> BytesIO:
    all_responses = _opo_json_response(chunks)
    output_pdf = BytesIO()

    for enum_index, response_index in enumerate(range(len(all_responses["questions"]))):
        write_to_txt(
            str(enum_index + 1)
            + ". "
            + all_responses["questions"][response_index]
            + "\n",
            output_pdf,
        )

        for answer_index, answer in enumerate(
            range(len(all_responses["answers"][response_index]))
        ):
            final_answer = all_responses["answers"][response_index][answer]
            if search_test_letter(final_answer):
                write_to_txt(final_answer, output_pdf)
            else:
                write_to_txt(ENUM_LIST[answer_index] + ") " + final_answer, output_pdf)
        write_to_txt("", output_pdf)

    write_to_txt("***SOLUCIONES***", output_pdf)
    for enum_index, response_index in enumerate(
        range(len(all_responses["correct_response"]))
    ):
        response_number = f"Solución pregunta número {enum_index + 1}:"
        write_to_txt(
            response_number + " " + all_responses["correct_response"][response_index],
            output_pdf,
        )

    output_pdf.seek(0)
    return output_pdf


def return_generated_PDF(text):
    formated_text = delete_bloq(text)
    formated_text = delete_word_regex(formated_text, "Subir")
    chunks = extract_articles(formated_text)

    return write_chunk_return_pdf(chunks)

