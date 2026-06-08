import streamlit as st

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="EduTrack AI",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# VALIDAÇÃO DE LOGIN
# ==========================================

if "auth_token" not in st.session_state:
    st.warning("Faça login para acessar o sistema.")
    st.stop()

if not st.session_state.auth_token:
    st.warning("Faça login para acessar o sistema.")
    st.stop()

# ==========================================
# TÍTULO
# ==========================================

st.title("🎓 EduTrack AI")

st.caption(
    "Sistema acadêmico para gerenciamento de disciplinas e tarefas."
)

# ==========================================
# DASHBOARD
# ==========================================

st.subheader("🏠 Dashboard")

st.write(
    "Bem-vindo ao seu assistente acadêmico."
)

col1, col2 = st.columns(2)

col1.metric(
    "Disciplinas",
    "Em desenvolvimento"
)

col2.metric(
    "Tarefas",
    "Em desenvolvimento"
)

st.info(
    "Utilize o menu lateral para acessar Disciplinas, Tarefas e Perfil."
)