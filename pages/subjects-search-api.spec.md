# subjects-search-api Specification

## Purpose
Define um endpoint de busca para a tabela `subjects`, permitindo a filtragem por nome e a identificação de disciplinas com tarefas atrasadas.

## ADDED Requirements

### Requirement: Criar endpoint de busca para disciplinas
O sistema SHALL fornecer um endpoint `GET /subjects/search` que permite a busca e filtragem de disciplinas.

#### Scenario: Busca por nome de disciplina
- **WHEN** um usuário autenticado envia uma requisição `GET` para `/subjects/search` com o parâmetro `name`.
- **THEN** o sistema SHALL retornar uma lista de disciplinas do usuário cujo nome contenha o valor do parâmetro `name`.

#### Scenario: Filtrar por disciplinas com tarefas atrasadas
- **WHEN** um usuário autenticado envia uma requisição `GET` para `/subjects/search` com o parâmetro `has_overdue_tasks=true`.
- **THEN** o sistema SHALL buscar todas as `academic_tasks` do usuário onde `due_date` é anterior à data atual e `status` não é "completed".
- **AND** o sistema SHALL retornar uma lista das disciplinas (`subjects`) únicas associadas a essas tarefas atrasadas.

#### Scenario: Combinar busca por nome e filtro de tarefas atrasadas
- **WHEN** um usuário autenticado envia uma requisição `GET` para `/subjects/search` com os parâmetros `name` e `has_overdue_tasks=true`.
- **THEN** o sistema SHALL retornar uma lista de disciplinas que satisfaçam ambos os critérios para aquele usuário.

#### Scenario: Busca sem parâmetros
- **WHEN** um usuário autenticado envia uma requisição `GET` para `/subjects/search` sem parâmetros de filtro.
- **THEN** o sistema SHALL retornar todas as disciplinas associadas ao usuário, comportamento idêntico ao do endpoint `GET /subjects`.

#### Scenario: Usuário não autorizado
- **WHEN** uma requisição é feita sem autenticação.
- **THEN** o sistema SHALL retornar um erro de "Unauthorized".