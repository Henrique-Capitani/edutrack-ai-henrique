import requests

# URL BASE DA API
BASE_URL = "https://x8ki-letl-twmt.n7.xano.io/api:edutrack"

# ==================================================
# SUBJECTS
# ==================================================

# LISTAR DISCIPLINAS
def get_subjects():

    try:

        response = requests.get(
            f"{BASE_URL}/subjects"
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }

# CRIAR DISCIPLINA
def add_subject(name, professor, carga_horaria):

    try:

        data = {
            "name": name,
            "professor": professor,
            "carga_horaria": carga_horaria
        }

        response = requests.post(
            f"{BASE_URL}/subjects",
            json=data
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }

# ==================================================
# TASKS
# ==================================================

# LISTAR TAREFAS
def get_tasks():

    try:

        response = requests.get(
            f"{BASE_URL}/tasks"
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }

# CRIAR TAREFA
def add_task(title, description, deadline, status):

    try:

        data = {
            "title": title,
            "description": description,
            "deadline": deadline,
            "status": status
        }

        response = requests.post(
            f"{BASE_URL}/tasks",
            json=data
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }