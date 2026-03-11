# \# EduTrack AI

# \*\*Projeto da disciplina Innovation Lab – Faculdade Impacta\*\*

# \* \*\*Aluno:\*\* Henrique Capitani

# \* \*\*Ano:\*\* 2025/2026

# 

# \### Tecnologias Utilizadas

# \* Git \& GitHub

# \* VS Code

# \* Node.js

# \* OpenSpec

# \* Xano

# 

# \---

# 

# \# Referências de Design e Estrutura - EduTrack AI

# 

# \## 1. Exploração no Figma (UI/UX)

# 

# \*\*Template 1: Education \& LMS Dashboard UI\*\*

# \* \*\*Link:\*\* https://www.figma.com/community/file/exemplo-lms-dashboard-123

# \* \*\*Por que é útil:\*\* Achei o layout muito limpo. A forma como o menu lateral (sidebar) está organizado facilita a navegação entre "Disciplinas" e "Tarefas". Os cards de resumo com as métricas do aluno dão uma visão rápida do progresso, o que será ótimo para a tela inicial do EduTrack AI.

# 

# \*\*Template 2: Student Task Manager\*\*

# \* \*\*Link:\*\* https://www.figma.com/community/file/exemplo-student-task-456

# \* \*\*Por que é útil:\*\* Gostei bastante de como as tarefas pendentes são listadas. Eles usam um sistema de \*checkboxes\* simples com tags de prioridade e datas de entrega. Essa interface direta ao ponto é ideal para a nossa funcionalidade de gerenciamento de tarefas.

# 

# \---

# 

# \## 2. Exploração no Xano (Backend)

# 

# \* \*\*Modelagem de Dados:\*\* Analisei as documentações dos Starter Templates de \*Authentication\* e \*Task Management\* no Marketplace do Xano. 

# \* \*\*Principais Sacadas:\*\* A estrutura de tabelas relacionais é muito bem feita. Entendi que precisaremos de uma tabela separada para `Users` (alunos) conectada à tabela de `Tasks` (tarefas) e `Courses` (disciplinas) através de chaves estrangeiras. Isso garante que cada aluno veja apenas as suas próprias tarefas e matérias quando a API for conectada ao Streamlit.

