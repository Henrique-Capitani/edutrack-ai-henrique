api subjects/{subjects_id} {
  // Endpoint para deletar uma disciplina específica.
  @DELETE

  // 1. Busca o registro da disciplina pelo ID fornecido na URL.
  //    - Importante: A busca já filtra pelo 'user_id' do usuário autenticado
  //      para garantir que um usuário não possa sequer encontrar (e, portanto, deletar)
  //      a disciplina de outro.
  get subjects as subject {
    id = inputs.subjects_id;
    user_id = auth.id;
  }

  // 2. Se o registro foi encontrado (o que implica que ele pertence ao usuário),
  //    deleta o registro da tabela 'subjects'.
  //    Se não foi encontrado, a função 'get' acima já terá retornado um erro 404.
  delete subject;

  // 3. Retorna uma resposta de sucesso vazia, indicando que a operação foi concluída.
  return null;
}