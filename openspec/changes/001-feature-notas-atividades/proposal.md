# Proposta: Lançamento de Notas em Atividades

## Why
Atualmente, o sistema não permite que professores registrem as notas dos alunos em atividades acadêmicas. Para centralizar a gestão de desempenho e fornecer feedback quantitativo, é essencial que os professores possam lançar essas notas na plataforma.

## What Changes
Esta mudança introduz a capacidade de registrar notas. As seguintes alterações serão feitas:
1.  **Nova Tabela (`activity_grades`):** Uma nova tabela será criada para armazenar a nota de um aluno para uma atividade específica, incluindo quem lançou a nota.
2.  **Nova API (`POST /activity_grades`):** Um novo endpoint será criado para permitir o registro (lançamento) de uma nova nota na tabela `activity_grades`.

## Impact
- **Backend:** O schema do banco de dados será estendido com a tabela `activity_grades` e uma nova rota de API será adicionada para a criação de registros de notas.
- **Frontend:** Nenhum impacto direto, mas habilita o desenvolvimento de futuras interfaces para que professores possam lançar notas e alunos possam visualizá-las.
- **Segurança:** A nova API deverá garantir que apenas usuários autenticados e com a permissão adequada (ex: professor da disciplina) possam lançar notas.
