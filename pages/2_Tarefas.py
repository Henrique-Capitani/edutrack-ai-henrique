import streamlit as st

st.set_page_config(
    page_title="Tarefas",
    page_icon="📝"
)

st.title("📝 Minhas Tarefas")

# COLUNAS
col1, col2 = st.columns([3, 1])

with col1:

    busca = st.text_input(
        "Buscar tarefa...",
        placeholder="Ex: Estudar Python"
    )

with col2:

    filtro = st.selectbox(
        "Status",
        [
            "Todas",
            "Pendente",
            "Em andamento",
            "Concluída"
        ]
    )

st.markdown("---")

# TAREFA 1
with st.expander(
    "📌 Estudar Streamlit",
    expanded=True
):

    st.write("**Disciplina:** Frontend")

    st.write("**Prazo:** 25/05/2026")

    st.checkbox(
        "Marcar como concluída",
        value=False
    )

# TAREFA 2
with st.expander(
    "📌 Fazer atividade de Banco de Dados"
):

    st.write("**Disciplina:** Banco de Dados")

    st.write("**Prazo:** 28/05/2026")

    st.checkbox(
        "Marcar como concluída",
        value=True
    )