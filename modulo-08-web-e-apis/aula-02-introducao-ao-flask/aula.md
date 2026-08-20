# Aula 2 — Introdução ao Flask

**Objetivos desta aula:**
- Criar uma API básica com Flask.
- Definir rotas com diferentes métodos HTTP.
- Ler parâmetros de URL e corpo da requisição (JSON).
- Testar a API com o `test_client()` do próprio Flask.

## O que é Flask

Flask é um *microframework* web para Python — "micro" porque traz o
essencial (roteamento de URLs, requisições, respostas) sem impor uma
estrutura rígida de projeto, deixando você adicionar só o que precisar.
É uma ótima porta de entrada para desenvolvimento web em Python.

## Uma API mínima

```python
# arquivo: app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "API de tarefas no ar!"

if __name__ == "__main__":
    app.run(debug=True)
```

Rodando `python3 app.py`, o Flask inicia um servidor local (por padrão em
`http://127.0.0.1:5000`). `debug=True` reinicia o servidor
automaticamente quando o código muda, e mostra tracebacks detalhados em
caso de erro — útil em desenvolvimento, **nunca** em produção.

## Rotas com JSON

```python
from flask import Flask, jsonify

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Estudar Python", "concluida": False},
]

@app.route("/tarefas")
def listar_tarefas():
    return jsonify(tarefas)
```

`jsonify()` converte uma estrutura Python (lista, dicionário) em uma
resposta HTTP com `Content-Type: application/json` — o equivalente,
dentro do Flask, ao `json.dumps` que vimos no módulo 5.

## Parâmetros na URL

```python
@app.route("/tarefas/<int:id_tarefa>")
def buscar_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404
```

`<int:id_tarefa>` captura a parte da URL como inteiro e passa como
argumento para a função da rota. Retornar uma tupla `(corpo, status)`
define o código de status da resposta — aqui, `404` quando não
encontrada.

## Recebendo dados no corpo (POST)

```python
from flask import request

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()          # lê o corpo JSON da requisição
    novo_id = max((t["id"] for t in tarefas), default=0) + 1
    nova_tarefa = {"id": novo_id, "titulo": dados["titulo"], "concluida": False}
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201
```

Por padrão, uma rota só aceita `GET`. `methods=["POST"]` habilita o
método `POST` para essa rota específica.

## Atualizando e removendo

```python
@app.route("/tarefas/<int:id_tarefa>", methods=["PUT"])
def atualizar_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            dados = request.get_json()
            tarefa["titulo"] = dados.get("titulo", tarefa["titulo"])
            tarefa["concluida"] = dados.get("concluida", tarefa["concluida"])
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas/<int:id_tarefa>", methods=["DELETE"])
def remover_tarefa(id_tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t["id"] != id_tarefa]
    return "", 204
```

## Testando com `test_client()`

O Flask fornece um cliente de teste que simula requisições HTTP **sem**
precisar de um servidor de verdade rodando em uma porta — ideal para
testes automatizados (relembrando `pytest`, módulo 6):

```python
def test_listar_tarefas():
    cliente = app.test_client()
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200
    assert isinstance(resposta.get_json(), list)

def test_criar_tarefa():
    cliente = app.test_client()
    resposta = cliente.post("/tarefas", json={"titulo": "Nova tarefa"})
    assert resposta.status_code == 201
    assert resposta.get_json()["titulo"] == "Nova tarefa"
```

## Erros comuns

- Deixar `debug=True` em produção — expõe informações internas do
  código em caso de erro, um risco de segurança real.
- Esquecer que `request.get_json()` retorna `None` se o cliente não
  enviar `Content-Type: application/json` — sempre valide antes de usar
  os dados.
- Modificar uma lista global (`tarefas`) diretamente em cada rota sem
  cuidado — em uma aplicação real, isso seria substituído por um banco
  de dados (próxima aula da persistência).

## Boas práticas

- Devolva sempre o código de status apropriado (`201` ao criar, `404`
  quando não encontrar, `204` ao remover sem conteúdo).
- Valide os dados recebidos antes de usá-los (o módulo de FastAPI, na
  próxima aula, mostra uma forma mais automática de fazer isso).
- Escreva testes com `test_client()` para cada rota, cobrindo o caminho
  feliz e os casos de erro (recurso não encontrado, dados inválidos).

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Fundamentos de HTTP e REST](../aula-01-fundamentos-http-e-rest/aula.md) · ➡️ [Próxima aula: Introdução ao FastAPI](../aula-03-introducao-ao-fastapi/aula.md)
