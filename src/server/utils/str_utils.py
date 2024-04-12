import os
import re
from typing import List


def extract_articles(texto: str) -> List[str]:
    articles = re.findall(
        r"(Artículo\s\d+\..*?)(?=Artículo\s\d+\.|\Z)", texto, re.DOTALL
    )

    return articles


def delete_word_regex(text: str, word: str) -> str:
    pattern = r"\b{}\b".format(re.escape(word))
    result = re.sub(pattern, "", text)

    return result


def delete_bloq(text: str) -> str:
    clean_text = re.sub(r"\[Bloque \d+: #[^\]]+\]", "", text)

    return clean_text


def extract_title_from_path(file_path: str) -> str:
    filename = os.path.basename(file_path)
    title = filename.split("/")[-1].split(".")[0]
    return title


def search_test_letter(text: str) -> bool:
    regex = r"[A-Za-z]\)"
    has = re.findall(regex, text)

    return bool(has)
