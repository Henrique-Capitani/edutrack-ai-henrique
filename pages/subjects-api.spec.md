# subjects-api Specification

## Purpose
Define os endpoints da API RESTful para criar, ler, atualizar e deletar (CRUD) registros na tabela `subjects`, garantindo que os usuários só possam acessar seus próprios dados.

## Requirements

### Requirement: Criar uma nova disciplina
O sistema SHALL fornecer um endpoint `POST /subjects` para criar uma nova disciplina.

#### Scenario: Usuário cria uma disciplina com sucesso
- **WHEN** um usuário autenticado envia uma requisição `POST` para `/subjects` com o nome da disciplina.
- **THEN** o sistema SHALL criar um novo registro na tabela `subjects`, associando-o ao `user_id` do usuário autenticado.

### Requirement: Listar as disciplinas do usuário
O sistema SHALL fornecer um endpoint `GET /subjects` para listar as disciplinas.

#### Scenario: Usuário lista suas disciplinas
- **WHEN** um usuário autenticado envia uma requisição `GET` para `/subjects`.
- **THEN** o sistema SHALL retornar uma lista contendo apenas as disciplinas associadas ao `user_id` do usuário autenticado.

### Requirement: Atualizar uma disciplina
O sistema SHALL fornecer um endpoint `PATCH /subjects/{id}` para atualizar uma disciplina existente.

#### Scenario: Usuário atualiza sua própria disciplina
- **WHEN** um usuário autenticado envia uma requisição `PATCH` para `/subjects/{id}` com novos dados.
- **THEN** o sistema SHALL verificar se a disciplina pertence ao usuário.
- **AND** se pertencer, o sistema SHALL atualizar o registro correspondente.

### Requirement: Deletar uma disciplina
O sistema SHALL fornecer um endpoint `DELETE /subjects/{id}` para deletar uma disciplina.

#### Scenario: Usuário deleta sua própria disciplina
- **WHEN** um usuário autenticado envia uma requisição `DELETE` para `/subjects/{id}`.
- **THEN** o sistema SHALL verificar se a disciplina pertence ao usuário.
- **AND** se pertencer, o sistema SHALL remover o registro correspondente da tabela `subjects`.