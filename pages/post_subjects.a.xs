api subjects {
  // Endpoint para criar uma nova disciplina.
  // A disciplina é automaticamente associada ao usuário autenticado.
  @POST
  
  inputs {
    // O nome da disciplina a ser criada.
    text name;
  }

  // 1. Adiciona um novo registro na tabela 'subjects'.
  //    - Associa o 'user_id' do registro ao ID do usuário autenticado.
  //    - Define o 'name' da disciplina com base no input.
  create subjects as subject {
    user_id = auth.id;
    name = inputs.name;
  }

  // 2. Retorna o registro da disciplina recém-criada.
  return subject;
}