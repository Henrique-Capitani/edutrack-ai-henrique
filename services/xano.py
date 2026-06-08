import requests

# URL BASE DA API
BASE_URL = "https://x8ki-letl-twmt.n7.xano.io/api:edutrack"

# ==================================================
# SUBJECTS
# ==================================================

def get_subjects(token):

    try:

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(
            f"{BASE_URL}/subjects",
            headers=headers
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


def add_subject(
    token,
    name,
    professor,
    carga_horaria
):

    try:

        data = {
            "name": name,
            "professor": professor,
            "carga_horaria": carga_horaria
        }

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.post(
            f"{BASE_URL}/subjects",
            json=data,
            headers=headers
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


# ==================================================
# TASKS
# ==================================================

def get_tasks(token):

    try:

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(
            f"{BASE_URL}/tasks",
            headers=headers
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }


def add_task(
    token,
    title,
    description,
    deadline,
    status
):

    try:

        data = {
            "title": title,
            "description": description,
            "deadline": deadline,
            "status": status
        }

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.post(
            f"{BASE_URL}/tasks",
            json=data,
            headers=headers
        )

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }