import streamlit as st
import numpy as np
import pandas as pd

# --- Configuração da Página ---
st.set_page_config(layout='wide')

# --- Título da página ---
st.title('Aula de st.tabs()')

# --- Criar as abas ---
abas = st.tabs(['Gráfico', 'Formulário', 'Dados'])

# --- Trabalhar com as abas ---
with abas[0]:
    st.header('Visualização com Gráficos')

    dados_linha = pd.DataFrame({
        'Semana': ['S1', 'S2', 'S3', 'S4', 'S5'],
        'Vendas': [10,12,8,15,18]
    }).set_index('Semana') # Eixo X

    st.subheader('Gráfico de linha')
    st.line_chart(dados_linha)

    dados_barras = pd.DataFrame({
        'Produto': ['Mouse', 'Teclado', 'Monitor', 'Fone', 'Gabinete'],
        'Valor': [50, 150.0, 500, 200.00, 300.0]
    }).set_index('Produto') # Eixo X

    st.subheader('Gráfico de Barras')
    st.bar_chart(dados_barras)

    dados_area = pd.DataFrame(
        np.random.rand(20,3),
        columns=['Canal A', 'Canal B', 'Canal C']
    )

    st.subheader('Gráfico Área')
    st.area_chart(dados_area)

    with abas[1]:
        st.header('Cadastro')
        st.write('')

        with st.form('Formulário_usuario'):
            nome = st.text_input('Nome:')
            email = st.text_input('e-mail:')
            idade = st.number_input('Idade', min_value=0, max_value=100)
            enviar = st.form_submit_button('Enviar')

        if enviar:
            st.success('Dados enviados com sucesso!')
            st.header('Dados do cliente:')
            st.subheader(f'Nome: {nome}')
            st.subheader(f'E-mail: {email}')
            st.subheader(f'Idade: {idade}')
        
    with abas[2]:
        st.header('Visualização de Dados')
        st.write('Tabela e filtrso simples')

        dados = {
            'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor'],
            'Preço': [4500, 120, 250, 900],
            'Estoque': [10, 50, 30, 20]
        }

        filtro_preco = st.slider('Preço máximo:', 0, 5000, 5000)

        dados_filtrados = {
            c: [v[i] for i in range(len(dados['Preço'])) if dados['Preço'][i] <= filtro_preco]
            for c, v in dados.items()
        }

        st.dataframe(dados_filtrados)
