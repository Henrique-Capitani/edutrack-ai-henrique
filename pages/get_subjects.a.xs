api subjects {
  // Endpoint para listar todas as disciplinas do usuário autenticado.
  @GET

  // 1. Busca todos os registros na tabela 'subjects'.
  query all subjects as subjects_list {
    // 2. Filtra os resultados para retornar apenas as disciplinas
    //    que pertencem ao usuário atualmente autenticado (auth.id).
    filter by subjects.user_id == auth.id;
  }

  // 3. Retorna a lista de disciplinas encontradas.
  return subjects_list;
}