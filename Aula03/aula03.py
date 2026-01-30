# --- importando as bibliotecas ---
import numpy as np
import pandas as pd
import streamlit as st


# --- Título da página ---
st.title("Trabalhando com Dados e Gráficos")

# --- Cabeçalho --- 
st.header('Gerando e Exibindo Dados Aleatórios')

# --- Gerar um DataFrame (df) de exemplo ---
df = pd.DataFrame(
    np.random.randn(20, 3), # 20 linhas e 3 colunas com números aleatórios 
    columns = ['col1', 'col2', 'col3'] # Nome das colunas
)

# --- Exibir o DataFrame de forma interativa ---
st.subheader('Um DataFrame gerado aleatoriamente:')
st.dataframe(df)

# --- Exibir os gráficos com o DataFrame gerado ----
st.subheader("Gráficos")
st.line_chart(df) # gráfico de linha
st.bar_chart(df) # gráfico de barras
st.area_chart(df) # gráfico de área
st.scatter_chart(df) # gráfico de dispersão

# --- Exemplo com upload de arquivos ---
st.subheader("Carregando arquivo csv")
upload = st.file_uploader(
    label='Anexar arquivo csv:',
    type='csv'
)

if upload is not None:

    try:
        # ---- Mostrar um perdaço do arquivo ---
        df_upload = pd.read_csv(upload)
        st.success('Arquivo carregado com sucesso!')
        st.write('As primeiras 10 linhas do seu arquivo:')
        st.dataframe(df_upload.head(10)) # Mostrará 10 linhas.

        # --- Tentar plotar as duas primeiras colunas se existirem ---
        if df_upload.shape[1] >= 2:
            st.subheader ('Gráfico das duas primeiras colunas:')
            st.line_chart(df_upload.iloc[:, :2])
        
        else:
            st.info("Seu arquivo tem menos de 2 colunas")
        
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}.")

