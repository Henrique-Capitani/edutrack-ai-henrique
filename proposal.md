# Proposta: Script de Cálculo de Progresso

## Why
Atualmente, o sistema não possui uma maneira automatizada de calcular e exibir o progresso do aluno com base em suas tarefas acadêmicas. É necessário um script que possa processar uma lista de tarefas e retornar uma métrica de progresso (porcentagem de tarefas concluídas) para ser usada em dashboards e relatórios.

## What Changes
Esta mudança introduz um novo script de utilidade para o cálculo de progresso.

1.  **Novo Script (`scripts/calculate_progress.py`):** Será criado um script Python que recebe uma lista de tarefas, calcula a porcentagem de tarefas concluídas e retorna o resultado em formato JSON.

## Impact
- **Backend:** Nenhum impacto direto no esquema do banco de dados. Adiciona um novo script de lógica de negócios.
- **Frontend:** O script poderá ser invocado pela aplicação Streamlit para exibir visualizações de progresso para os alunos.