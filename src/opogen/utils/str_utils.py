import re

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

def search_test_letter(text):
    regex = r"[A-Za-z]\)"
    has = re.findall(regex, text)

    return bool(has)
