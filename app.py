import streamlit as st
import database as db

# Configuração da Página (Título na aba do navegador)
st.set_page_config(page_title="EduTrack AI", page_icon="🎓")

# Título Principal
st.title("🎓 EduTrack AI")

# Sidebar (Menu Lateral)
st.sidebar.header("Menu")
menu_option = st.sidebar.radio("Navegar", ["Dashboard", "Disciplinas", "Tarefas"])

# Inicializa o banco de dados local de disciplinas
db.init_db()

current_user_id = st.sidebar.text_input("ID do usuário", value="1")
st.sidebar.caption("Use este ID para filtrar e gerenciar suas disciplinas.")
current_user_id = current_user_id.strip() or "anonymous"

# Conteúdo Dinâmico
if menu_option == "Dashboard":
    st.write("Bem-vindo ao seu assistente acadêmico!")
    st.info("Conecte ao Xano para ver seus dados reais.")
    
    # Exemplo de Métrica Visual
    subjects = db.get_subjects(current_user_id)
    col1, col2 = st.columns(2)
    col1.metric("Disciplinas Ativas", str(sum(1 for s in subjects if s["is_active"])))
    col2.metric("Tarefas Pendentes", "0")

elif menu_option == "Disciplinas":
    st.subheader("Minhas Disciplinas")
    st.write(f"Disciplinas cadastradas para o usuário: `{current_user_id}`")

    subjects = db.get_subjects(current_user_id)
    if not subjects:
        st.info("Nenhuma disciplina cadastrada para este usuário ainda.")
    else:
        for subject in subjects:
            status = "Ativa" if subject["is_active"] else "Inativa"
            st.markdown(f"**{subject['name']}**")
            st.write(f"Código: {subject['code'] or '_não informado_' }")
            st.write(f"Descrição: {subject['description'] or '_sem descrição_' }")
            st.write(f"Status: {status}")
            st.write("---")

    with st.form("new_subject_form"):
        st.subheader("Cadastrar nova disciplina")
        name = st.text_input("Nome da disciplina")
        code = st.text_input("Código da disciplina")
        description = st.text_area("Descrição")
        is_active = st.checkbox("Disciplina ativa", value=True)
        create_subject = st.form_submit_button("Adicionar disciplina")
        if create_subject:
            if not name.strip():
                st.error("O nome da disciplina é obrigatório.")
            else:
                db.add_subject(current_user_id, name, code, description, is_active)
                st.success("Disciplina adicionada com sucesso.")
                st.experimental_rerun()

elif menu_option == "Tarefas":
    st.subheader("Gerenciamento de Tarefas")
    st.checkbox("Exemplo: Estudar Streamlit")