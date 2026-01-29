import streamlit as st

# --- Título da aula ---

st.title("Elementos Interativos de Layout")

# --- Barra lateral (IMPORTANTE!) ---

st.sidebar.header("Opções da aplicação")
nome = st.sidebar.text_input(label='Digite seu nome')
st.sidebar.write(f'Olá, {nome}')

# --- Colunas para organizar a tela principal ---

# Quantidade de colunas que a tela principal terá
colunas = st.columns(2)

# Escolhendo em qual parte da coluna iremos escrever, escolhendo a primeira coluna.
with colunas[0]:
    st.header("Interações simples")
    if st.button("Me aperte!"):
        st.success("Você clicou no botão!")
    
    valor_slider = st.slider(
        label='Selecione um valor: ',
        min_value=0,
        max_value=100,
    )

    st.write(f'O valor selecionado no slider é: {valor_slider}')

# Escolhendo a segunda coluna.
with colunas[1]:

    st.header("Informações e imagem")
    st.info("Está é uma mensagem usando 'st.info'.")

    # --- Colocando uma imagem com URL ---
    st.image(
        image='https://cdn.pixabay.com/photo/2016/05/04/08/58/wifi-transparent-1371033_640.png',
        caption='Logo WIFI',
        use_container_width=True
    )

    st.warning("Atenção: AVISO!")

# --- Entrada de número e exibição ---

numero = st.number_input(
    label='Digite um número', 
    min_value=2,
    max_value=30
)

st.write(f'Você digitou o número: {numero}')
