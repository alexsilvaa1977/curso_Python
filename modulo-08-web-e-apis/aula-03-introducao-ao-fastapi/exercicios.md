# Exercícios — Aula 3: Introdução ao FastAPI

1. Adicione um campo `prioridade: int = 1` ao modelo `NovaTarefa` e ao
   modelo `Tarefa`, e ajuste `criar_tarefa()` para usá-lo.

2. Adicione uma rota `GET /tarefas/pendentes` que retorna apenas as
   tarefas com `concluida == False`.

3. Escreva um teste que confirme que enviar `{"titulo": "X", "concluida": "não é booleano"}`
   para `POST /tarefas` resulta em `422` (validação de tipo do
   Pydantic).

4. Adicione uma rota `GET /tarefas/contagem` que retorna
   `{"total": N, "concluidas": X}`.

5. Compare (em um comentário) o código necessário para validar que
   `titulo` não pode ser vazio nesta aula (FastAPI/Pydantic) com o que
   seria necessário fazer manualmente no Flask (aula anterior).

6. **Desafio:** adicione um segundo recurso `/usuarios` com seu próprio
   modelo Pydantic (`nome: str`, `email: str`), rotas de listar/criar/
   buscar, e pelo menos 4 testes cobrindo casos de sucesso e validação.

---
⬅️ [Voltar para a aula](aula.md)
