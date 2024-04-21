import os
import streamlit as st

AVAILIBLE_MODELS = ["gpt-3.5-turbo-instruct", "gpt-4-turbo-preview"]

def ask_for_password():
    entered_password = st.sidebar.text_input("Introduce la contrasena para acceder a la aplicacion", type="password")
    
    if entered_password == os.environ.get["PASSWORD"]:
        st.empty()
    else:
        st.stop()

def select_gpt_model():
    model = st.sidebar.selectbox("Selecciona un modelo para generar tu documento",options=AVAILIBLE_MODELS)
    return model

def init_session_state():
    if "pdf_bytes" not in st.session_state:
        st.session_state["pdf_bytes"] = None
