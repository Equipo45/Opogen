import uuid
import streamlit as st

from config import config
from llm.llm_service import init_config

from utils.response_utils import return_generated_PDF
from utils.file_utils import load_file_auto_detect, remove_final_extension

init_config(config)

uploaded_file = st.file_uploader('Carga tu archivo PDF', type=["pdf","docx","txt"])
if uploaded_file is not None:
    random_uuid_str = str(uuid.uuid4())
    st.write(uploaded_file)
    pdf_str_data = load_file_auto_detect(uploaded_file = uploaded_file)
    pdf_byte_data = return_generated_PDF(pdf_str_data, random_uuid_str+"_"+remove_final_extension(uploaded_file.name))
    st.download_button("Descagar tu archivo generado!", pdf_byte_data, "OPOGEN_"+uploaded_file.name, mime = "application/pdf")
    