from utils.file_utils import load_file_auto_detect
from utils.str_utils import extract_articles, delete_word_regex, delete_bloq
from llm.llm_service import init_config
from config import config
from utils.response_utils import write_chunk_to_pdf
from flask import Flask, jsonify
from flask_cors import CORS


READ_FILE_PATH = "src/opogen/read_files/OBJETO Y AMBITO DE APLICACION DE LA LEY 31-1995 DEL 8 DE NOVIEMBRE.docx"

def main():
    init_config(config)

    text = load_file_auto_detect(READ_FILE_PATH)
    formated_text = delete_bloq(text)
    formated_text = delete_word_regex(formated_text, "Subir")
    chunks = extract_articles(formated_text)
    write_chunk_to_pdf(chunks)

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/generador_examen', methods=['GET'])
def exam_generator():
    return jsonify({
        'status': 'success',
        'generated_examn': "Examen generado satisfactoriamente!" 
    })

if __name__ == '__main__':
    app.run(debug=True)