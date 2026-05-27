table academic_tasks {
  description = "Armazena as tarefas acadêmicas dos alunos, como lições, provas e trabalhos.";

  table_reference users {
    rename = "user_id";
  }

  table_reference subjects {
    rename = "subject_id";
  }

  text title;

  text description?;

  date due_date?;

  text status? = "pending";
}