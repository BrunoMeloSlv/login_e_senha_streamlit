import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Vendas", layout="wide")

usuarios = pd.read_csv(r"C:\Users\Bruno Melo\Downloads\usuarios.txt")
vendas = pd.read_excel(r"C:\Users\Bruno Melo\Downloads\vendas.xlsx")

def autenticar(usuario, senha):
    user = usuarios[
                    (usuarios['usuario'] == usuario) &
                    (usuarios['senha'] == senha) 
                    ]
    
    if not user.empty:
        return user.iloc[0]['vendedor']
    return None

if 'logado' not in st.session_state:
    st.session_state.logado = False
    st.session_state.vendedor = None

if not st.session_state.logado:

    st.title('🔐 Login')

    usuario = st.text_input('Usuário')
    senha = st.text_input('Senha', type='password')

    if st.button('Entrar'):
        vendedor = autenticar(usuario, senha)

        if vendedor:
            st.session_state.logado = True
            st.session_state.vendedor = vendedor
            st.success(f'Bem-vindo, {vendedor}')
        else:
            st.error("Usuário ou senha inválidos")
else:
    vendedor = st.session_state.vendedor

    st.title(f"📊 Dashboard - {vendedor}")

    # Botão logout
    if st.button("Sair"):
        st.session_state.logado = False
        st.session_state.vendedor = None
        st.rerun()

    # Filtrar dados
    df_vendedor = vendas[vendas["vendedor"] == vendedor]

    st.subheader("Suas vendas")
    st.dataframe(df_vendedor)

    # Métricas
    total_vendas = df_vendedor["valor"].sum()
    qtd_vendas = len(df_vendedor)

    col1, col2 = st.columns(2)
    col1.metric("Total vendido", f"R$ {total_vendas:,.2f}")
    col2.metric("Quantidade de vendas", qtd_vendas)     
