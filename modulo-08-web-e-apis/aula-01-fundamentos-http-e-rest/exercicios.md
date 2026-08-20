# Exercícios — Aula 1: Fundamentos de HTTP e REST

1. Para cada operação abaixo, escreva o método HTTP e a URL corretos,
   seguindo o estilo REST, para uma API de "produtos":
   - Listar todos os produtos.
   - Buscar o produto com id 10.
   - Criar um novo produto.
   - Remover o produto com id 10.

2. Para cada situação, diga qual código de status HTTP seria mais
   apropriado: (a) um recurso foi criado com sucesso; (b) o cliente
   pediu um recurso que não existe; (c) o servidor teve um erro
   inesperado; (d) uma remoção foi bem-sucedida e não há nada a
   devolver.

3. Usando o servidor local da aula como base, adicione um novo caminho
   `GET /status` que devolve `{"status": "ok"}` com código `200`.

4. Adicione ao servidor local um segundo recurso simulado (por exemplo,
   `/produtos`) com sua própria lista de dados fixos.

5. Explique, em um comentário, por que `GET /deletar-tarefa?id=5` é
   considerado um mau design de API REST, e como ele deveria ser
   reescrito.

6. **Desafio:** modifique o servidor da aula para também aceitar
   `POST /tarefas`, lendo o corpo da requisição (JSON) e adicionando uma
   nova tarefa ao dicionário `tarefas` (dica: use `self.rfile.read(int(self.headers["Content-Length"]))`
   dentro de um método `do_POST`). Teste com
   `requests.post(url, json={...})`.

---
⬅️ [Voltar para a aula](aula.md)
