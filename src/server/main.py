from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

from utils.file_utils import write_chunk_to_pdf

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/generate_exam", methods=["POST"])
def exam_generator():
    if "file" not in request.files:
        return jsonify(
            {"status": "error", "message": "No file part in the request"}
        ), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"status": "error", "message": "No selected file"}), 400

    try:
        pdf_content = write_chunk_to_pdf(file)
        pdf_content.seek(0)

        return send_file(
            pdf_content,
            attachment_filename="generated_exam.pdf",
            as_attachment=True,
        )
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
