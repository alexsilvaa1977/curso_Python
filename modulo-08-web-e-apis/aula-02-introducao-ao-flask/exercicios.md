# Exercícios — Aula 2: Introdução ao Flask

1. Adicione uma rota `GET /tarefas/pendentes` que retorna apenas as
   tarefas com `concluida == False`.

2. Adicione um teste em `test_app.py` para a rota do exercício 1.

3. Adicione validação em `criar_tarefa()`: se o campo `"titulo"` não
   for enviado no corpo da requisição, devolva `400` com uma mensagem de
   erro, em vez de deixar o código quebrar.

4. Adicione uma rota `GET /tarefas/contagem` que retorna
   `{"total": N, "concluidas": X, "pendentes": Y}`.

5. Escreva um teste que verifique que criar uma tarefa sem `"titulo"`
   retorna `400` (relacionado ao exercício 3).

6. **Desafio:** adicione um segundo recurso à API, `/usuarios`, com
   `GET` (listar), `POST` (criar) e `GET /usuarios/<id>` (buscar um).
   Escreva pelo menos 4 testes cobrindo esse novo recurso.

---
⬅️ [Voltar para a aula](aula.md)
