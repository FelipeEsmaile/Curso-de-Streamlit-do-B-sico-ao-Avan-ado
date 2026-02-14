import streamlit as st

# --- Importa as páginas (que criamos em outra pasta) ---
from pages import pagina_inicial, analise_dados


st.sidebar.title('Navegação')
pagina = st.sidebar.radio(
    label='Ir para',
    options=['Página Inicial','Análise']
)

# --- Verificar qual página foi selecionada ---
if pagina == 'Página Inicial':
    pagina_inicial.pagina_inicial() # o primeiro "pagina_inicial" é o arquivo. O segundo é a função demtro do arquivo.

if pagina == 'Análise':
    analise_dados.analise_dados() 