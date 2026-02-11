import streamlit as st
import time

# --- Configurações da página ---
st.set_page_config(
    page_title = 'Customização do App',
    page_icon='',
    layout='wide'
)

# --- Título da página ----
st.title('Customização e Componentes')

# --- Explicação do Site ---
st.markdown(""" Esta aplicação demonstra a tematização e a ideia de componente customizados.
             As cores e fontes que você vê agora são definidas no arquivo `.streamlit/congif.toml`
            """)

# --- Exemplo de st.status ---
st.header('Mensagem de status')
with st.status('Preparando dados...', expanded=True) as status:
    st.write("Buscando dados da fonte...")
    time.sleep(1)
    st.write("Processando Informações...")
    time.sleep(2)
    st.write("Gerando relatório final...")
    time.sleep(3)
    status.update(label='Dados carregados!', state='complete')
st.success('Processo concluído!')