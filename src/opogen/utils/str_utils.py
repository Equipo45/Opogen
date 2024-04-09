import re
import os

def extract_articles(texto):
    articles = re.findall(r'(Artículo\s\d+\..*?)(?=Artículo\s\d+\.|\Z)', texto, re.DOTALL)
    
    return articles
    
def delete_word_regex(text, word):
    pattern = r'\b{}\b'.format(re.escape(word))
    result = re.sub(pattern, '', text)
    
    return result

def delete_bloq(text):
    clean_text = re.sub(r'\[Bloque \d+: #[^\]]+\]', '', text)

    return clean_text

def extract_title_from_path(file_path):
    filename = os.path.basename(file_path)
    title = filename.split('/')[-1].split('.')[0]
    return title

def search_test_letter(text):
    regex = r"[A-Za-z]\)"
    has = re.findall(regex, text)

    return bool(has)
