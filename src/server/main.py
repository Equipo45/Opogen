import uuid
import streamlit as st

from utils.response_utils import return_generated_PDF
from utils.file_utils import load_file_auto_detect, remove_final_extension
from utils.frame_utils import ask_for_password, select_gpt_model

ask_for_password()
model = select_gpt_model()

with st.form("my-form", clear_on_submit=True):
    
    uploaded_file = st.file_uploader('Carga tu archivo PDF', type=["pdf","docx","txt"])
    submitted = st.form_submit_button("ENVIAR!")
    
    if submitted and uploaded_file is not None:
        
        random_uuid_str = str(uuid.uuid4())
        pdf_str_data = load_file_auto_detect(uploaded_file = uploaded_file)
        
        with st.spinner("Creando tu examen de oposicion, esto tomara un momento..."):
            pdf_byte_data = return_generated_PDF(pdf_str_data, random_uuid_str+"_"+remove_final_extension(uploaded_file.name), model)
        st.toast("¡Examen generador satisfactoriamente!")
        
if submitted:
    st.download_button("¡Descagar tu archivo generado!", pdf_byte_data, "OPOGEN_DOCUMENTO.pdf", mime = "application/pdf",use_container_width=True)