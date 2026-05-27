import streamlit as st
import requests

# ====================================
# CONFIGURAÇÕES API
# ====================================

LOGIN_URL = "https://x8ki-letl-twmt.n7.xano.io/api:92pcNBqE/auth/login"

SIGNUP_URL = "https://x8ki-letl-twmt.n7.xano.io/api:92pcNBqE/auth/signup"

# ====================================
# CONFIGURAÇÃO DA PÁGINA
# ====================================

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# ====================================
# SESSÃO
# ====================================

if "auth_token" not in st.session_state:
    st.session_state.auth_token = None

if "usuario_id" not in st.session_state:
    st.session_state.usuario_id = None

# ====================================
# TÍTULO
# ====================================

st.title("🔐 EduTrack Login")

aba = st.radio(
    "Escolha uma opção:",
    ["Login", "Criar Conta"]
)

# ====================================
# LOGIN
# ====================================

if aba == "Login":

    st.subheader("Entrar")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):

        payload = {
            "email": email,
            "password": senha
        }

        response = requests.post(
            LOGIN_URL,
            json=payload
        )

        if response.status_code == 200:

            dados = response.json()

            st.session_state.auth_token = dados["authToken"]
            st.session_state.usuario_id = dados["user_id"]

            st.success("Login realizado com sucesso!")

            st.page_link(
                "home.py",
                label="Ir para Home",
                icon="🏠"
            )

        else:

            st.error("Email ou senha inválidos.")

# ====================================
# CRIAR CONTA
# ====================================

if aba == "Criar Conta":

    st.subheader("Criar Conta")

    nome = st.text_input("Nome")
    novo_email = st.text_input("Novo Email")
    nova_senha = st.text_input(
        "Nova Senha",
        type="password"
    )

    if st.button("Cadastrar"):

        payload = {
            "name": nome,
            "email": novo_email,
            "password": nova_senha
        }

        response = requests.post(
            SIGNUP_URL,
            json=payload
        )

        if response.status_code == 200:

            dados = response.json()

            st.session_state.auth_token = dados["authToken"]
            st.session_state.usuario_id = dados["user_id"]

            st.success("Conta criada com sucesso!")

            st.page_link(
                "home.py",
                label="Ir para Home",
                icon="🏠"
            )

        else:

            st.error("Erro ao criar conta.")
