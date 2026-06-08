import streamlit as st
import requests

# ==========================================
# LOGIN
# ==========================================

if "auth_token" not in st.session_state:
    st.warning("Faça login primeiro.")
    st.stop()

# ==========================================
# CONFIG
# ==========================================

API_TASKS = "https://x8ki-letl-twmt.n7.xano.io/api:edutrack/tasks"
API_SUBJECTS = "https://x8ki-letl-twmt.n7.xano.io/api:edutrack/subjects"

headers = {
    "Authorization": f"Bearer {st.session_state.auth_token}"
}

# ==========================================
# TÍTULO
# ==========================================

st.title("📝 Minhas Tarefas")

# ==========================================
# CARREGAR DISCIPLINAS
# ==========================================

subjects_response = requests.get(
    URL_SUBJECTS,
    headers=headers
)

disciplinas = []

if subjects_response.status_code == 200:
    disciplinas = subjects_response.json()

# ==========================================
# NOVA TAREFA
# ==========================================

with st.expander("➕ Nova Tarefa"):

    titulo = st.text_input("Título")

    descricao = st.text_area("Descrição")

    prazo = st.date_input("Prazo")

    status = st.selectbox(
        "Status",
        [
            "pending",
            "in_progress",
            "completed"
        ]
    )

    disciplina_escolhida = st.selectbox(
        "Disciplina",
        disciplinas,
        format_func=lambda x: x["name"]
    ) if disciplinas else None

    if st.button("Salvar Tarefa"):

        if not disciplina_escolhida:

            st.error("Selecione uma disciplina.")

        else:

            payload = {
                "title": titulo,
                "description": descricao,
                "deadline": str(prazo),
                "status": status,
                "subject_id": disciplina_escolhida["id"]
            }

            response = requests.post(
                URL_TASKS,
                json=payload,
                headers=headers
            )

            if response.ok:

                st.success(
                    "Tarefa criada com sucesso!"
                )

                st.rerun()

            else:

                st.error(
                    f"Erro ao criar tarefa: {response.text}"
                )
# ==========================================
# FILTROS
# ==========================================

col1, col2 = st.columns(2)

with col1:

    busca = st.text_input(
        "Buscar tarefa"
    )

with col2:

    filtro_status = st.selectbox(
        "Status",
        [
            "Todos",
            "pending",
            "in_progress",
            "completed"
        ]
    )

# ==========================================
# CARREGAR TAREFAS
# ==========================================

response = requests.get(
    URL_TASKS,
    headers=headers
)

if response.status_code == 429:

    st.warning(
        "Limite temporário do plano gratuito do Xano atingido. Aguarde alguns segundos e tente novamente."
    )

    st.stop()

elif response.status_code != 200:

    st.error(
        f"Erro ao carregar tarefas ({response.status_code})"
    )

    st.stop()

tarefas = response.json()

# ==========================================
# FILTROS FRONT
# ==========================================

if busca:

    tarefas = [
        t for t in tarefas
        if busca.lower()
        in t["title"].lower()
    ]

if filtro_status != "Todos":

    tarefas = [
        t for t in tarefas
        if t["status"] == filtro_status
    ]

# ==========================================
# LISTAGEM
# ==========================================

st.success(
    f"{len(tarefas)} tarefa(s) encontrada(s)"
)

for tarefa in tarefas:

    with st.container(border=True):

        st.subheader(
            tarefa["title"]
        )

        st.write(
            tarefa["description"]
        )

        st.write(
            f"📅 Prazo: {tarefa['deadline']}"
        )

        st.write(
            f"📌 Status: {tarefa['status']}"
        )

        col1, col2 = st.columns(2)

        # ==================================
        # EDITAR
        # ==================================

        with col1:

            with st.popover(
                f"✏️ Editar #{tarefa['id']}"
            ):

                novo_titulo = st.text_input(
                    "Título",
                    value=tarefa["title"],
                    key=f"titulo_{tarefa['id']}"
                )

                nova_desc = st.text_area(
                    "Descrição",
                    value=tarefa["description"],
                    key=f"desc_{tarefa['id']}"
                )

                novo_status = st.selectbox(
                    "Status",
                    [
                        "pending",
                        "in_progress",
                        "completed"
                    ],
                    index=[
                        "pending",
                        "in_progress",
                        "completed"
                    ].index(
                        tarefa["status"]
                    ),
                    key=f"status_{tarefa['id']}"
                )

                if st.button(
                    "Salvar Alterações",
                    key=f"editar_{tarefa['id']}"
                ):

                    payload = {
                        "title": novo_titulo,
                        "description": nova_desc,
                        "status": novo_status
                    }

                    edit_response = requests.patch(
                        f"{URL_TASKS}/{tarefa['id']}",
                        json=payload,
                        headers=headers
                    )

                    if edit_response.status_code == 200:

                        st.success(
                            "Tarefa atualizada!"
                        )

                        st.rerun()

                    else:

                        st.error(
                            edit_response.text
                        )

        # ==================================
        # EXCLUIR
        # ==================================

        with col2:

            if st.button(
                "🗑 Excluir",
                key=f"delete_{tarefa['id']}"
            ):

                delete_response = requests.delete(
                    f"{URL_TASKS}/{tarefa['id']}",
                    headers=headers
                )

                if delete_response.status_code in [200, 204]:

                    st.success(
                        "Tarefa removida!"
                    )

                    st.rerun()

                else:

                    st.error(
                        delete_response.text
                    )