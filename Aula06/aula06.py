import streamlit as st
from datetime import date, time

st.title('Widgets Avançados de Entrada')

st.header('Seleção de opções')

# --- Caixa de Seleção ---
opcao_selecionada = st.selectbox(
    label='Qual tipo de ranqueamento você escolherá? ',
    options=(
        '-',
        'Priorizar Vistoria',
        'Condição Técnica',
        'Condicionamento Social',
        'Análise Integrada'
    )
)

st.write(f'Você escolheu: {opcao_selecionada}')

# --- Multiseleção ---
multiplas_opcoes = st.multiselect(
    label='Quais frutas você vai escolher?',
    options=[
        'Laranja',
        'Maça',
        'Tangerina',
        'Uva',
        'Coco',
        'Morango',
        'Melancia'
    ],
    placeholder='Selecione as frutas'
)

st.write(f'Você gosta de: {",".join(multiplas_opcoes) if multiplas_opcoes else 'Nenhuma'}')

# --- Radio button ---
ranque = st.radio(
    label='Qual tipo de ranqueamento você irá escolher?',
    options=(
        'Priorizar Vistoria',
        'Condições Técnicas',
        'Condições Sociais',
        'Análise Integrada'
    )
)

st.write(f'Tipo de ranqueamento selecionado: {ranque}.')

# --- Selecionar a data ---
data = st.date_input(
     label='Selecione uma data:',
     value=date.today()
)
st.write(f"Data selecionada: {data}")

# --- Selecionar a hora ---
hora = st.time_input(
    label='Selecione uma hora:',
    value=time(12,0)
)
st.write(f"Hora selecionada: {hora}")

# --- Caixa de Seleção e botão de download ---
termos = st.checkbox('Eu aceito os termos e condições.')
if termos:
    st.success('Termos aceitos!')
    st.download_button(
        label='Baixar relatório',
        data='Conteúdo do relatório de exemplo.',
        file_name='relatorio_exemplo.txt',
        mime='text/plain'
    )
else:
    st.info('Por favor, aceite os termos.')

# --- Formulário com st.form ---
with st.form('meu_formulário_contado'):
    st.write('Preencha os seus dados:')
    nome = st.text_input('Nome: ')
    email = st.text_input('E-mail: ')
    mensagem = st.text_area('Mensagem: ')
    submissao = st.form_submit_button('Enviar mensagem')

    if submissao: 
        if nome and email and mensagem:
            st.success(f'Mensagem de {nome} enviada com sucesso.')
            st.write(f'E-mail: {email}')
            st.write(f'Mensagem: {mensagem}')
        else:
            st.error('Por favor, peencha todos os campos do formulário.')
    