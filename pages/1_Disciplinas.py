import streamlit as st
import requests

st.title("EduTrack - Disciplinas")

# Campo de busca
nome_disciplina = st.text_input("Buscar disciplina")

# Botão
if st.button("Buscar"):

    # URL da API
    url = "https://x8ki-letl-twmt.n7.xano.io/api:edutrack/search"

    # Dados enviados
    params = {
        "name": nome_disciplina,
        "has_overdue_tasks": False
    }

    # Token
    headers = {
        "Authorization": "Bearer SEU_TOKEN_AQUI"
    }

    # Requisição
    response = requests.get(url, params=params, headers=headers)

    # Resultado
    if response.status_code == 200:
        disciplinas = response.json()

        if disciplinas:
            for d in disciplinas:
                st.success(f"""
                📚 {d['name']}
                
                👨‍🏫 Professor: {d['professor']}
                
                ⏰ Carga Horária: {d['carga_horaria']}
                """)
        else:
            st.warning("Nenhuma disciplina encontrada.")

    else:
        st.error("Erro ao buscar disciplinas.")