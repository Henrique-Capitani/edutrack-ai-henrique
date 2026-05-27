import streamlit as st

st.set_page_config(
    page_title="Perfil",
    page_icon="👤"
)

st.title("👤 Meu Perfil")

st.subheader("Informações do Usuário")

with st.form("form_perfil"):

    nome = st.text_input(
        "Nome Completo",
        value="Henrique Capitani Silva"
    )

    email = st.text_input(
        "E-mail",
        value="henrique.capitani@aluno.impacta.edu.br"
    )

    senha = st.text_input(
        "Nova Senha",
        type="password"
    )

    salvar = st.form_submit_button(
        "Salvar Alterações"
    )

    if salvar:

        st.success(
            "Perfil atualizado com sucesso!"
        )

st.markdown("---")

st.info(
    "Aqui futuramente ficará a integração com autenticação do Xano."
)