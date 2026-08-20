# Aula 1 — Fundamentos de HTTP e REST

**Objetivos desta aula:**
- Entender o modelo cliente-servidor e o protocolo HTTP.
- Conhecer os métodos HTTP mais usados (`GET`, `POST`, `PUT`, `DELETE`)
  e os principais códigos de status.
- Entender os princípios do estilo arquitetural REST.

## Cliente e servidor

Toda vez que você acessa um site ou um app faz uma chamada de API, existe
um **cliente** (seu navegador, seu celular, outro programa) fazendo um
**pedido** (*request*) a um **servidor**, que processa e devolve uma
**resposta** (*response*). HTTP (*HyperText Transfer Protocol*) é o
protocolo — o "conjunto de regras" — que define como esse pedido e essa
resposta são formatados.

```
Cliente                          Servidor
   |  ---- GET /produtos/42 --->   |
   |                                | (processa o pedido)
   |  <--- 200 OK + dados ------   |
```

## Métodos HTTP

Cada pedido HTTP tem um **método**, que indica a intenção da operação:

| Método | Uso típico |
|---|---|
| `GET` | buscar/ler um recurso, sem alterar nada no servidor |
| `POST` | criar um novo recurso |
| `PUT` | atualizar um recurso existente (substituindo ele por completo) |
| `PATCH` | atualizar parcialmente um recurso existente |
| `DELETE` | remover um recurso |

```
GET /tarefas          -- listar todas as tarefas
GET /tarefas/5         -- buscar a tarefa com id 5
POST /tarefas           -- criar uma nova tarefa
PUT /tarefas/5           -- substituir a tarefa 5 por completo
DELETE /tarefas/5         -- remover a tarefa 5
```

## Códigos de status

Toda resposta HTTP vem com um código numérico de 3 dígitos, indicando o
resultado do pedido:

| Faixa | Significado | Exemplos comuns |
|---|---|---|
| 2xx | Sucesso | `200 OK`, `201 Created`, `204 No Content` |
| 3xx | Redirecionamento | `301 Moved Permanently` |
| 4xx | Erro do cliente | `400 Bad Request`, `404 Not Found`, `401 Unauthorized` |
| 5xx | Erro do servidor | `500 Internal Server Error` |

Alguns dos mais usados no dia a dia de uma API:
- `200 OK`: pedido processado com sucesso.
- `201 Created`: um novo recurso foi criado (resposta típica de `POST`).
- `204 No Content`: sucesso, mas sem conteúdo para devolver (comum em
  `DELETE`).
- `400 Bad Request`: o pedido está malformado (dados inválidos).
- `404 Not Found`: o recurso pedido não existe.
- `500 Internal Server Error`: algo quebrou no servidor.

## Corpo do pedido/resposta e JSON

Além do método e da URL, um pedido pode ter um **corpo** (*body*) — os
dados enviados. Em APIs modernas, o formato mais comum é JSON (módulo
5):

```
POST /tarefas
Content-Type: application/json

{
  "titulo": "Estudar Python",
  "concluida": false
}
```

A resposta também costuma vir em JSON:

```
200 OK
Content-Type: application/json

{
  "id": 1,
  "titulo": "Estudar Python",
  "concluida": false
}
```

## O que é REST

REST (*Representational State Transfer*) é um estilo arquitetural para
projetar APIs web, baseado em alguns princípios centrais:

1. **Recursos identificados por URLs**: cada "coisa" que a API expõe
   (uma tarefa, um usuário, um produto) tem uma URL própria
   (`/tarefas/5`, não `/pegar_tarefa?id=5`).
2. **Uso correto dos métodos HTTP**: `GET` para ler, `POST` para criar,
   `PUT`/`PATCH` para atualizar, `DELETE` para remover — em vez de usar
   sempre `POST` para tudo.
3. **Sem estado no servidor** (*stateless*): cada pedido contém toda a
   informação necessária para ser processado; o servidor não depende de
   "lembrar" pedidos anteriores daquele cliente.
4. **Representações**: o cliente troca dados com o servidor através de
   representações (geralmente JSON) do recurso, não do recurso "em si".

## Um exemplo de API REST bem desenhada (tarefas)

```
GET    /tarefas          -> lista todas as tarefas
GET    /tarefas/5         -> detalhes da tarefa 5
POST   /tarefas            -> cria uma nova tarefa
PUT    /tarefas/5           -> atualiza a tarefa 5 por completo
DELETE /tarefas/5            -> remove a tarefa 5
```

Compare com uma API mal desenhada, que não segue REST:

```
POST /pegarTarefas
POST /pegarTarefaPorId?id=5
POST /criarTarefa
POST /atualizarTarefa?id=5
POST /removerTarefa?id=5
```

A segunda versão "funciona", mas força quem consome a API a ler
documentação para entender cada operação, em vez de aproveitar
convenções já conhecidas de método HTTP + URL do recurso.

## Erros comuns

- Usar `GET` para operações que alteram dados no servidor (ex.:
  `GET /deletar_tarefa?id=5`) — `GET` deve ser seguro para repetir
  quantas vezes quiser, sem efeitos colaterais.
- Ignorar códigos de status e sempre devolver `200 OK`, mesmo em caso de
  erro — dificulta que o cliente saiba se o pedido realmente funcionou.
- Criar URLs com verbos (`/criarTarefa`, `/deletarTarefa`) em vez de
  usar o método HTTP correto sobre o recurso (`POST /tarefas`,
  `DELETE /tarefas/5`).

## Boas práticas

- Modele URLs em torno de **recursos** (substantivos: `/tarefas`), não
  de ações (verbos: `/criarTarefa`).
- Use o método HTTP correto para cada operação.
- Devolva o código de status que realmente representa o resultado
  (`404` quando não encontrar, `201` quando criar, etc.).

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-08-web-e-apis/aula-01-fundamentos-http-e-rest/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Voltar ao índice do módulo](../README.md) · ➡️ [Próxima aula: Introdução ao Flask](../aula-02-introducao-ao-flask/aula.md)
