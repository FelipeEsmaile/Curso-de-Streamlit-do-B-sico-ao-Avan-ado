# Duas entradas de números e 4 botões com as principais operações básicas de mátematica
# e o usuário escolher umas das 4. Tendo um texto mostrando o resultado.

import streamlit as st

n1 = st.number_input(
    label="Digite um número",
    format='%0f'
)

n2 = st.number_input(
    label="Digite um segundo número",
    format='%0f'
)

st.header("Escolha uma opção:")

colunas = st.columns(4)

with colunas[0]: 
    if st.button(label='SOMA',use_container_width=True):
        soma = n1 + n2
        st.success(f"O resultado da soma é: {soma}")

with colunas[1]: 
    if st.button(label='SUBTRAÇÃO',use_container_width=True): 
        subtração = n1 - n2
        st.success(f"O resultado da subtração é: {subtração}")

with colunas[2]:   
    if st.button(label='MULTIPLICAÇÃO', use_container_width=True):
        multi = n1*n2
        st.success(f"O resultado da multiplicação é: {multi}")

with colunas[3]: 
    if st.button(label='DIVISÃO',use_container_width=True):
        div = n1/n2
        st.success(f"O resultado da divisão é: {div}")