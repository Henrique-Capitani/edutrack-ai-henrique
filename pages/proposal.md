# Proposta: Endpoint de Busca para Disciplinas

## Why
Atualmente, o usuário pode apenas listar todas as suas disciplinas. Não há uma maneira eficiente de encontrar uma disciplina específica por nome ou de identificar rapidamente quais disciplinas exigem atenção imediata (por terem tarefas atrasadas). Um endpoint de busca avançada é necessário para melhorar a usabilidade e o gerenciamento das responsabilidades acadêmicas.

## What Changes
Esta mudança introduz um novo endpoint de API para busca e filtragem de disciplinas.

1.  **Novo Endpoint (`GET /subjects/search`):** Será criado um endpoint que permite filtrar disciplinas com base em dois critérios:
    - `name`: Para buscar disciplinas por parte do nome.
    - `has_overdue_tasks`: Para filtrar disciplinas que contenham tarefas com data de entrega vencida e status diferente de "completed".

## Impact
- **Backend:** Será adicionada uma nova API no Xano com lógica de consulta mais complexa, envolvendo a verificação cruzada entre as tabelas `subjects` e `academic_tasks`. A integração com lógica Python pode ser necessária se a consulta se tornar muito complexa para ser executada nativamente no Xano.
- **Frontend:** Habilita a criação de uma interface de busca e filtro na aplicação Streamlit, permitindo que os usuários encontrem disciplinas de forma mais dinâmica.
- **Segurança:** O endpoint deverá garantir rigorosamente que todas as consultas retornem apenas dados pertencentes ao usuário autenticado.