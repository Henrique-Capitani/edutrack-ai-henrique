# Tasks for 'feature-notas-atividades'

- [x] (Xano) Criar a tabela `activity_grades` com os seguintes campos: `user_id` (relação com user), `academic_task_id` (relação com academic_tasks), `grade` (número), e `created_by` (relação com user).
- [x] (Xano) Criar o endpoint `POST /activity_grades` que recebe `user_id`, `academic_task_id` e `grade`, valida as permissões do usuário autenticado (professor) e cria um novo registro na tabela `activity_grades`.
