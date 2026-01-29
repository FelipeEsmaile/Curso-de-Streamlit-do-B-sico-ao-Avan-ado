# --- Importar o Streamlit ---

import streamlit as st

# --- Título da Página ---

st.title("Hello World.\nMinha primeira ação em streamlit.")

# --- Cabeçalho ---

st.header("Cabeçalho da Página")

# --- Subcabeçalho ---

st.subheader("Subcabeçalho")

# --- Texto normal ---

st.write("Um texto normal/comum")

# --- Texto com Markdown ---

st.markdown('''
Este é um exemplo de Markdown com **Negrito** e *itálico*.
Também podemos gerar listas:
* Item 1
* Item 2
* Item 3 ''')

# --- Texto literal ?? ---

st.text("Um texto 'literal', aqui não funciona as marcações do markdown.")