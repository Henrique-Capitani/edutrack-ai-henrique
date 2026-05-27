import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="EduTrack AI",
    page_icon="🎓",
    layout="wide"
)

# TÍTULO PRINCIPAL
st.title("🎓 EduTrack AI")

st.caption(
    "Sistema acadêmico para gerenciamento de disciplinas e tarefas."
)

# SIDEBAR
st.sidebar.header("Menu")

menu_option = st.sidebar.radio(
    "Navegar",
    [
        "Dashboard",
        "Disciplinas",
        "Tarefas"
    ]
)

# ==========================================
# DASHBOARD
# ==========================================

if menu_option == "Dashboard":

    st.write("Bem-vindo ao seu assistente acadêmico!")

    st.info("Conecte ao Xano para ver seus dados reais.")

    col1, col2 = st.columns(2)

    col1.metric(
        "Disciplinas Ativas",
        "0"
    )

    col2.metric(
        "Tarefas Pendentes",
        "0"
    )

# ==========================================
# DISCIPLINAS
# ==========================================

elif menu_option == "Disciplinas":

    st.subheader("📚 Minhas Disciplinas")

    # FORMULÁRIO
    with st.form(
        "new_subject_form",
        clear_on_submit=True
    ):

        st.write("Adicionar nova disciplina")

        subject_name = st.text_input(
            "Nome da Disciplina"
        )

        submitted = st.form_submit_button(
            "Adicionar"
        )

        # SALVAR
        if submitted:

            from services.xano import add_subject

            result = add_subject(subject_name)

            if "error" in result:

                st.error(result["error"])

            else:

                st.success(
                    f"Disciplina '{subject_name}' adicionada!"
                )

    # LISTAR DISCIPLINAS
    from services.xano import get_subjects

    subjects = get_subjects()

    if "error" in subjects:

        st.error(subjects["error"])

    elif subjects:

        for subject in subjects:

            st.write(subject)

    else:

        st.write("Nenhuma disciplina encontrada.")

# ==========================================
# TAREFAS
# ==========================================

elif menu_option == "Tarefas":

    st.subheader("📝 Gerenciamento de Tarefas")

    st.checkbox(
        "Exemplo: Estudar Streamlit"
    )