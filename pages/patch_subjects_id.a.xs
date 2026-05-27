api subjects/{subjects_id} {
  // Endpoint para atualizar uma disciplina específica.
  @PATCH

  inputs {
    // O novo nome para a disciplina (opcional).
    text name?;
  }

  // 1. Busca o registro da disciplina pelo ID fornecido na URL.
  //    - Importante: A busca já filtra pelo 'user_id' do usuário autenticado
  //      para garantir que um usuário não possa encontrar (e, portanto, editar)
  //      a disciplina de outro.
  get subjects as subject {
    id = inputs.subjects_id;
    user_id = auth.id;
  }

  // 2. Se o registro foi encontrado (o que implica que ele pertence ao usuário),
  //    edita o registro com os novos dados fornecidos no input.
  //    Se não foi encontrado, a função 'get' acima já terá retornado um erro 404.
  edit subject {
    name = inputs.name;
  }

  // 3. Retorna o registro da disciplina atualizado.
  return subject;
}