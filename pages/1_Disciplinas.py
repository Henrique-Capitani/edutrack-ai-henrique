import streamlit as st
import requests

# Configurações da API Xano
BASE_URL = "https://x8ki-letl-twmt.n7.xano.io/api:edutrack/subjects"

st.title("📚 Gestão de Disciplinas")

# Verificação de Autenticação
if not st.session_state.get('auth_token'):
    st.warning("Por favor, realize o login para gerenciar disciplinas.")
    st.stop()

def get_headers():
    return {"Authorization": f"Bearer {st.session_state.get('auth_token', '')}"}

def get_subjects():
    try:
        response = requests.get(BASE_URL, headers=get_headers(), timeout=10)
        return response.json() if response.status_code == 200 else []
    except Exception as e:
        st.error(f"Erro ao conectar com Xano: {e}")
        return []

def add_subject(name):
    try:
        response = requests.post(BASE_URL, headers=get_headers(), json={"name": name}, timeout=10)
        return response
    except Exception as e:
        st.error(f"Erro de rede/conexão: {e}")
        return None

def update_subject(id, name):
    try:
        response = requests.patch(
            f"{BASE_URL}/{id}", 
            headers=get_headers(), 
            json={"name": name}, 
            timeout=10
        )
        return response
    except Exception as e:
        return None

def delete_subject(id):
    try:
        response = requests.delete(f"{BASE_URL}/{id}", headers=get_headers(), timeout=10)
        return response
    except Exception as e:
        return None

# --- Interface: Adicionar ---
with st.expander("➕ Adicionar Nova Disciplina"):
    with st.form("add_subject_form"):
        new_name = st.text_input("Nome da Disciplina")
        if st.form_submit_button("Salvar"):
            if new_name:
                res = add_subject(new_name)
                if res and res.ok:
                    st.success("Disciplina adicionada!")
                    st.rerun()
                else:
                    error_msg = res.text if res else "Servidor inacessível"
                    st.error(f"Erro ao adicionar: {error_msg}")

# --- Interface: Listagem e Ações ---
subjects = get_subjects()

if not subjects:
    st.info("Nenhuma disciplina encontrada.")
else:
    for sub in subjects:
        with st.container(border=True):
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.write(f"**{sub['name']}**")
            
            with col2:
                if st.button("Editar", key=f"edit_btn_{sub['id']}"):
                    st.session_state[f"editing_{sub['id']}"] = True
            
            with col3:
                if st.button("Excluir", key=f"del_btn_{sub['id']}", type="primary"):
                    res = delete_subject(sub['id'])
                    if res and res.ok:
                        st.success("Excluída!")
                        st.rerun()
                    else:
                        st.error("Erro ao excluir.")
            
            # Formulário de Edição Inline
            if st.session_state.get(f"editing_{sub['id']}", False):
                with st.form(key=f"form_edit_{sub['id']}"):
                    edit_name = st.text_input("Novo Nome", value=sub['name'])
                    if st.form_submit_button("Confirmar Alteração"):
                        res = update_subject(sub['id'], edit_name)
                        if res and res.ok:
                            st.session_state[f"editing_{sub['id']}"] = False
                            st.rerun()
                        else:
                            st.error("Erro ao atualizar.")