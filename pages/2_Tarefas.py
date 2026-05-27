import streamlit as st
import requests
from datetime import datetime

st.set_page_config(
    page_title="Tarefas",
    page_icon="📝"
)

# Configurações da API Xano
API_TASKS = "https://x8ki-letl-twmt.n7.xano.io/api:edutrack/tasks"
API_SUBJECTS = "https://x8ki-letl-twmt.n7.xano.io/api:edutrack/subjects"

st.title("📝 Minhas Tarefas")

# Verificação de Autenticação
if not st.session_state.get('auth_token'):
    st.warning("Por favor, realize o login para ver suas tarefas.")
    st.stop()

def get_headers():
    return {"Authorization": f"Bearer {st.session_state.get('auth_token', '')}"}

def get_data(url):
    try:
        resp = requests.get(url, headers=get_headers(), timeout=10)
        return resp.json() if resp.status_code == 200 else []
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return []

subjects = get_data(API_SUBJECTS)
tasks = get_data(API_TASKS)

# --- Adicionar Tarefa ---
with st.expander("➕ Nova Tarefa"):
    if not subjects:
        st.info("Crie uma disciplina primeiro.")
    else:
        with st.form("new_task"):
            t_title = st.text_input("Título")
            t_desc = st.text_area("Descrição")
            t_date = st.date_input("Data")
            sub_options = {s['name']: s['id'] for s in subjects}
            t_sub = st.selectbox("Disciplina", options=list(sub_options.keys()))
            
            if st.form_submit_button("Criar"):
                payload = {
                    "subject_id": sub_options[t_sub],
                    "title": t_title,
                    "description": t_desc,
                    "due_date": str(t_date),
                    "status": "pending"
                }
                response = requests.post(API_TASKS, headers=get_headers(), json=payload)
                if response.ok:
                    st.success("Tarefa criada!")
                    st.rerun()
                else:
                    st.error(f"Erro ao criar tarefa: {response.text}")

st.markdown("---")

# --- Listagem de Tarefas ---
if not tasks:
    st.info("Nenhuma tarefa encontrada.")
else:
    for t in tasks:
        with st.container(border=True):
            c1, c2 = st.columns([4, 1])
            with c1:
                st.subheader(t['title'])
                st.caption(f"Status: {t['status']} | Entrega: {t.get('due_date', 'S/D')}")
                if t.get('description'):
                    st.write(t['description'])
            
            with c2:
                if st.button("🗑️", key=f"del_{t['id']}"):
                    requests.delete(f"{API_TASKS}/{t['id']}", headers=get_headers(), timeout=10)
                    st.rerun()
                if st.button("✏️", key=f"edit_btn_{t['id']}"):
                    st.session_state[f"edit_task_{t['id']}"] = True

            # Form de Edição Inline
            if st.session_state.get(f"edit_task_{t['id']}", False):
                with st.form(f"f_edit_{t['id']}"):
                    new_t_title = st.text_input("Novo Título", value=t['title'])
                    new_status = st.selectbox("Status", ["pending", "in_progress", "completed"], 
                                            index=["pending", "in_progress", "completed"].index(t['status']))
                    if st.form_submit_button("Confirmar"):
                        try:
                            res = requests.patch(f"{API_TASKS}/{t['id']}", headers=get_headers(), 
                                         json={"title": new_t_title, "status": new_status}, timeout=10)
                            if res.ok:
                                st.session_state[f"edit_task_{t['id']}"] = False
                                st.rerun()
                        except Exception as e:
                            st.error(f"Erro ao atualizar: {e}")