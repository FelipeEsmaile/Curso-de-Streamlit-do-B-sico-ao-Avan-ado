import streamlit as st

# --- Criando o menu de navegação das páginas ---
pg = st.navigation(
    [
     st.Page('./pages/home.py', title='Página Inicial'), 
     st.Page('./pages/segunda_pagina.py', title='Segunda Página'),
     st.Page('./pages/terceira_pagina.py', title='Terceira Página')
    ],
    position='top'
)
pg.run()