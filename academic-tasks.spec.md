# academic-tasks Specification

## Purpose
Define a estrutura da tabela `academic_tasks` para permitir que os alunos gerenciem suas obrigações acadêmicas.

## Requirements

### Requirement: Criar a tabela academic_tasks
O sistema SHALL permitir o armazenamento de tarefas acadêmicas, associando cada tarefa a um usuário e a uma disciplina.

#### Scenario: Aluno cria uma nova tarefa
- **WHEN** um usuário cria uma nova tarefa acadêmica
- **THEN** o sistema deve armazená-la com os seguintes campos:
  - `user_id` (referência à tabela `users`)
  - `subject_id` (referência à tabela `subjects`)
  - `title` (texto, obrigatório)
  - `description` (texto, opcional)
  - `due_date` (data, opcional)
  - `status` (texto, com valor padrão "pending")

#### Scenario: Consulta de tarefas
- **WHEN** um usuário consulta suas tarefas
- **THEN** o sistema SHALL retornar apenas as tarefas associadas ao `user_id` do usuário autenticado.