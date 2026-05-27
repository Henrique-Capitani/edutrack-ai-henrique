import sys
import json

def calculate_progress(tasks):
    """
    Calcula o progresso com base em uma lista de tarefas.

    Args:
        tasks: Uma lista de dicionários de tarefas. Cada dicionário deve ter uma chave 'status'.

    Returns:
        Um dicionário contendo o total de tarefas, tarefas concluídas e a porcentagem de progresso.
    """
    if not isinstance(tasks, list):
        # Retorna um erro em formato JSON se a entrada não for uma lista
        return {"error": "A entrada esperada é uma lista de tarefas em formato JSON."}

    total_tasks = len(tasks)
    if total_tasks == 0:
        return {
            "total_tasks": 0,
            "completed_tasks": 0,
            "progress_percentage": 0.0
        }

    # Conta as tarefas que possuem o status 'completed'
    completed_tasks = sum(1 for task in tasks if task.get('status') == 'completed')
    
    progress_percentage = (completed_tasks / total_tasks) * 100

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "progress_percentage": round(progress_percentage, 2)
    }

def main():
    """
    Função principal para ler tarefas do stdin, calcular o progresso e imprimir o resultado em JSON.
    """
    input_data = json.load(sys.stdin)
    result = calculate_progress(input_data)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()