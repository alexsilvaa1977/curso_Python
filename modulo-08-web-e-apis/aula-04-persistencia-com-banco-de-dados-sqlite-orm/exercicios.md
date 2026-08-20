# Exercícios — Aula 4: Persistência com banco de dados: SQLite e ORM

1. Adicione uma coluna `prioridade` (Integer, `default=1`) ao modelo
   `TarefaDB`, e ajuste `criar_tarefa()` em `main.py` para aceitá-la.

2. Escreva uma consulta que retorna apenas as tarefas com
   `concluida == False`, usando `.filter()`.

3. Escreva uma função `contar_tarefas_por_status(sessao)` que retorna
   `{"concluidas": X, "pendentes": Y}` usando duas consultas `.count()`.

4. Adicione uma rota `DELETE /tarefas` (sem id) que remove **todas** as
   tarefas concluídas de uma vez, e escreva um teste para ela.

5. Modifique `test_main.py` para adicionar um teste que verifica que
   `GET /tarefas` retorna as tarefas na ordem em que foram criadas
   (`id` crescente).

6. **Desafio:** adicione um segundo modelo `UsuarioDB` (com `id`, `nome`,
   `email`) e uma coluna `usuario_id` em `TarefaDB` (uma relação de
   "cada tarefa pertence a um usuário", usando `ForeignKey` do
   SQLAlchemy). Escreva uma rota `GET /usuarios/{id}/tarefas` que
   retorna só as tarefas daquele usuário.

---
⬅️ [Voltar para a aula](aula.md) · ⬅️ [Voltar ao índice do módulo](../README.md)
