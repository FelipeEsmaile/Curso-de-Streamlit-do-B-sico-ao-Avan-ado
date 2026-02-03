# Criar um gerador de números aleatórios, onde ele mostra o número anterior zerado e o número atual.

import streamlit as st
from random import randint

# --- Título da página ---
st.title('Gerador de números aleatórios')

# --- Colocar na sessão o último número gerado ---
if 'ultimo_numero' not in st.session_state:
    st.session_state.ultimo_numero = 'Nenhum número foi gerado'

# --- Mostrar o último número gerado ---
st.subheader(f'último número gerado: {st.session_state.ultimo_numero}')

# --- Criar o botão para gerar o número aleatório ---
if st.button('Gerar'):
    num_gerado = randint(1,100)
    st.subheader(f'O número gerado foi: {num_gerado}')
    st.session_state.ultimo_numero = num_gerado