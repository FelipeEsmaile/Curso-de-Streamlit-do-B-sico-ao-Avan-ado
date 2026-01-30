# Mostre uma tabela com dados enviados pelo usuário (upload), pelo menos as primeiras 5 linhas. E mostrar 2 gráficos (linha e barra) 
# com esses dados.

import streamlit as st
import pandas as pd

st.title("Exercício 3")

# --- Fazer o upload de arquivos ---
st.subheader("Carregar arquivo:")
upload = st.file_uploader(
    label='Anexar arquivo:'
)

# Mostras as linhas e o gráficos
if upload is not None:

    try:
        df_upload = pd.read_csv(upload)
        st.success("Arquivo carregado com sucesso!")
        st.write("As primeiras 5 linhas do arquivo")
        st.dataframe(df_upload.head(5))
    
        if df_upload.shape[1] >= 2:
            st.subheader("Gráfico de Linhas das 2 primeiras colunas")
            st.line_chart(df_upload.iloc[:,:2])
            st.subheader("Gráfico de barras das 2 primeiras colunas")
            st.bar_chart(df_upload.iloc[:,:2])

        else:
            st.info("Seu arquivo tem menos 2 colunas")

    except Exception as e:
        st.error(f"Erro ao carregaro arquivo {e}")