import streamlit as st
import requests

# ==========================================
# LOGIN
# ==========================================

if "auth_token" not in st.session_state:
    st.warning("Faça login primeiro.")
    st.stop()

# ==========================================
# TÍTULO
# ==========================================

st.title("📚 Minhas Disciplinas")

# ==========================================
# API
# ==========================================

BASE_URL = "https://x8ki-letl-twmt.n7.xano.io/api:edutrack/subjects"


headers = {
    "Authorization": f"Bearer {st.session_state.auth_token}"
}

# ==========================================
# NOVA DISCIPLINA
# ==========================================

with st.expander("➕ Nova Disciplina"):

    nome = st.text_input("Nome da disciplina")

    professor = st.text_input("Professor")

    carga_horaria = st.number_input(
        "Carga Horária",
        min_value=1,
        step=1
    )

    if st.button("Salvar Disciplina"):

        payload = {
            "name": nome,
            "professor": professor,
            "carga_horaria": carga_horaria
        }

        response = requests.post(
            URL_SUBJECTS,
            json=payload,
            headers=headers
        )

        if response.status_code in [200, 201]:

            st.success(
                "Disciplina criada com sucesso!"
            )

            st.rerun()

        else:

            st.error(
                f"Erro ao criar disciplina ({response.status_code})"
            )

# ==========================================
# LISTAR DISCIPLINAS
# ==========================================

response = requests.get(
    URL_SUBJECTS,
    headers=headers
)

if response.status_code != 200:

    st.error(
        f"Erro ao carregar disciplinas ({response.status_code})"
    )

    st.stop()

disciplinas = response.json()

# ==========================================
# EXIBIÇÃO
# ==========================================

if not disciplinas:

    st.info(
        "Nenhuma disciplina cadastrada."
    )

else:

    st.success(
        f"{len(disciplinas)} disciplina(s) encontrada(s)"
    )

    for disciplina in disciplinas:

        with st.container(border=True):

            st.subheader(
                disciplina["name"]
            )

            st.write(
                f"👨‍🏫 Professor: {disciplina['professor']}"
            )

            st.write(
                f"⏰ Carga Horária: {disciplina['carga_horaria']}"
            )

            col1, col2 = st.columns(2)

            # ==========================================
            # EDITAR
            # ==========================================

            with col1:

                if st.button(
                    "✏️ Editar",
                    key=f"edit_{disciplina['id']}"
                ):

                    st.session_state[
                        "editar_disciplina"
                    ] = disciplina["id"]

            # ==========================================
            # EXCLUIR
            # ==========================================

            with col2:

                if st.button(
                    "🗑️ Excluir",
                    key=f"delete_{disciplina['id']}"
                ):

                    delete_url = (
                        f"{URL_SUBJECTS}/{disciplina['id']}"
                    )

                    delete_response = requests.delete(
                        delete_url,
                        headers=headers
                    )

                    if delete_response.status_code in [200, 204]:

                        st.success(
                            "Disciplina excluída."
                        )

                        st.rerun()

                    else:

                        st.error(
                            f"Erro ao excluir ({delete_response.status_code})"
                        )

            # ==========================================
            # FORMULÁRIO EDIÇÃO
            # ==========================================

            if st.session_state.get(
                "editar_disciplina"
            ) == disciplina["id"]:

                st.markdown("---")

                novo_nome = st.text_input(
                    "Nome",
                    value=disciplina["name"],
                    key=f"nome_{disciplina['id']}"
                )

                novo_professor = st.text_input(
                    "Professor",
                    value=disciplina["professor"],
                    key=f"prof_{disciplina['id']}"
                )

                nova_carga = st.number_input(
                    "Carga Horária",
                    value=int(
                        disciplina["carga_horaria"]
                    ),
                    key=f"carga_{disciplina['id']}"
                )

                col_salvar, col_cancelar = st.columns(2)

                with col_salvar:

                    if st.button(
                        "💾 Salvar Alterações",
                        key=f"save_{disciplina['id']}"
                    ):

                        patch_url = (
                            f"{URL_SUBJECTS}/{disciplina['id']}"
                        )

                        payload = {
                            "name": novo_nome,
                            "professor": novo_professor,
                            "carga_horaria": nova_carga
                        }

                        patch_response = requests.patch(
                            patch_url,
                            json=payload,
                            headers=headers
                        )

                        if patch_response.status_code == 200:

                            st.success(
                                "Disciplina atualizada com sucesso!"
                            )

                            del st.session_state[
                                "editar_disciplina"
                            ]

                            st.rerun()

                        else:

                            st.error(
                                f"Erro ao atualizar ({patch_response.status_code})"
                            )

                with col_cancelar:

                    if st.button(
                        "❌ Cancelar",
                        key=f"cancel_{disciplina['id']}"
                    ):

                        del st.session_state[
                            "editar_disciplina"
                        ]

                        st.rerun()