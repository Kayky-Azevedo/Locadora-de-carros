import streamlit as st

st.set_page_config(page_title="Tela de Login", page_icon="🔐")


def login(username, password):
    if username == 'admin' and password == "password123":
        return True
    else:
        return False


st.title("Acesso")

username = st.text_input("Nome de usuário")
password = st.text_input("Senha", type="password")

if st.button("Entrar"):
    if login(username, password):
        st.success(f"Bem-vindo, {username}")
    else:
        st.error("Nome de usuário ou senha incorretos")
