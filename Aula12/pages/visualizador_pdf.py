import streamlit as st

# --- Configurações da Página ---
st.set_page_config(page_title='Visualizador PDF', layout='centered')

# --- Título da Página ---
st.title('Visualizador de PDF')

# --- Campo para enviar o arquivo ---
upload = st.file_uploader(
    label ='Escolha um arquivo PDF',
    type='pdf'
)

# --- Mostrar o arquivo PDF no site ---

if upload is not None:
    st.pdf(upload, header=850)