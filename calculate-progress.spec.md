# calculate-progress Specification

## Purpose
Define o comportamento do script `scripts/calculate_progress.py`, responsável por calcular a porcentagem de progresso com base no status das tarefas acadêmicas.

## Requirements

### Requirement: Calcular a porcentagem de progresso das tarefas
O sistema SHALL fornecer um script que calcula o progresso com base nos status das tarefas.

#### Scenario: Cálculo com tarefas concluídas e pendentes
- **WHEN** o script `scripts/calculate_progress.py` é executado com uma lista de tarefas contendo status "completed" e outros.
- **THEN** o script SHALL calcular a porcentagem de tarefas com status "completed" em relação ao total de tarefas.
- **AND** o script SHALL retornar um objeto JSON contendo o total de tarefas, o número de tarefas concluídas e a porcentagem de progresso.

#### Scenario: Cálculo sem tarefas
- **WHEN** o script é executado com uma lista de tarefas vazia.
- **THEN** o script SHALL retornar um objeto JSON indicando 0 tarefas totais, 0 concluídas e 0% de progresso.