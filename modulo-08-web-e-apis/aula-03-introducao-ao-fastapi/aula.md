# Aula 3 — Introdução ao FastAPI

**Objetivos desta aula:**
- Criar uma API com FastAPI.
- Validar dados automaticamente com Pydantic.
- Entender a documentação automática (Swagger UI).
- Testar a API com `TestClient`.

## O que é FastAPI e por que ele se destaca

FastAPI é um framework web moderno para Python, construído sobre
`Starlette` (para a parte web) e `Pydantic` (para validação de dados).
Diferenciais em relação ao Flask:

- **Validação automática**: você declara o formato esperado dos dados
  com type hints (módulo 6), e o FastAPI valida sozinho, devolvendo
  erros claros quando os dados não conferem.
- **Documentação automática**: o FastAPI gera uma interface interativa
  (Swagger UI) para explorar e testar a API, sem esforço extra.
- **Assíncrono por padrão** (mas funções síncronas também funcionam
  normalmente, como nos exemplos desta aula).

## Modelando dados com Pydantic

```python
from pydantic import BaseModel

class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False
```

Um `BaseModel` do Pydantic é parecido com uma classe comum (módulo 4),
mas com validação automática de tipo: se alguém tentar criar uma
`Tarefa` com `titulo` que não seja `str`, o Pydantic recusa com um erro
claro, antes mesmo do seu código rodar.

## Uma API mínima com FastAPI

```python
# arquivo: main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool = False

tarefas = [Tarefa(id=1, titulo="Estudar Python", concluida=False)]

@app.get("/tarefas")
def listar_tarefas():
    return tarefas
```

Rodando com `uvicorn main:app --reload` (o servidor ASGI recomendado
para FastAPI), a API fica disponível, por padrão, em
`http://127.0.0.1:8000`. `--reload` reinicia automaticamente ao detectar
mudanças no código — útil em desenvolvimento.

## Documentação automática

Com o servidor rodando, acessar `http://127.0.0.1:8000/docs` no
navegador mostra uma interface interativa (Swagger UI) com todas as
rotas, os modelos esperados, e um botão para testar cada uma direto do
navegador — gerada automaticamente a partir do seu código, sem nenhuma
configuração extra.

## Parâmetros de rota e validação automática

```python
from fastapi import HTTPException

@app.get("/tarefas/{id_tarefa}")
def buscar_tarefa(id_tarefa: int):
    for tarefa in tarefas:
        if tarefa.id == id_tarefa:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
```

`id_tarefa: int` já garante que, se alguém acessar
`/tarefas/abc` (não numérico), o FastAPI devolve automaticamente um erro
`422 Unprocessable Entity` — sem você escrever nenhum código de
validação manual.

`HTTPException` é a forma do FastAPI de devolver um erro HTTP com
código e mensagem customizados (relembrando exceções, módulo 5 — aqui é
uma exceção especializada para o contexto de uma API web).

## Criando um recurso com corpo validado

```python
class NovaTarefa(BaseModel):
    titulo: str
    concluida: bool = False

@app.post("/tarefas", status_code=201)
def criar_tarefa(nova_tarefa: NovaTarefa):
    novo_id = max((t.id for t in tarefas), default=0) + 1
    tarefa = Tarefa(id=novo_id, titulo=nova_tarefa.titulo, concluida=nova_tarefa.concluida)
    tarefas.append(tarefa)
    return tarefa
```

Ao declarar `nova_tarefa: NovaTarefa` como parâmetro, o FastAPI:
1. Lê o corpo da requisição.
2. Valida que ele corresponde ao modelo `NovaTarefa`.
3. Se não corresponder (ex.: `titulo` ausente ou do tipo errado),
   devolve automaticamente `422` com detalhes de qual campo falhou —
   **sem você escrever nenhum `if`** de validação manual.

## Atualizando e removendo

```python
@app.put("/tarefas/{id_tarefa}")
def atualizar_tarefa(id_tarefa: int, dados: NovaTarefa):
    for tarefa in tarefas:
        if tarefa.id == id_tarefa:
            tarefa.titulo = dados.titulo
            tarefa.concluida = dados.concluida
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.delete("/tarefas/{id_tarefa}", status_code=204)
def remover_tarefa(id_tarefa: int):
    global tarefas
    tarefas = [t for t in tarefas if t.id != id_tarefa]
```

## Testando com `TestClient`

```python
from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)

def test_listar_tarefas():
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200

def test_criar_tarefa_sem_titulo_falha_validacao():
    resposta = cliente.post("/tarefas", json={})   # falta "titulo"
    assert resposta.status_code == 422
```

Note o segundo teste: como `titulo` é obrigatório no modelo
`NovaTarefa`, enviar um corpo vazio já é suficiente para o FastAPI
recusar o pedido automaticamente, sem nenhum código de validação escrito
por você.

## Erros comuns

- Esquecer `status_code=201`/`204` nas rotas de criação/remoção — por
  padrão, o FastAPI devolve `200` para toda rota que não especifica um
  status diferente.
- Confundir o modelo usado para **entrada** (o que o cliente envia, sem
  `id`, já que ele é gerado pelo servidor) com o modelo de **saída** (que
  inclui o `id`) — nesta aula, por simplicidade, usamos `NovaTarefa`
  para entrada e `Tarefa` (com `id`) para as tarefas armazenadas.
- Rodar `uvicorn` sem `--reload` durante o desenvolvimento e ter que
  reiniciar manualmente a cada mudança.

## Boas práticas

- Deixe o Pydantic validar os dados de entrada — evite reimplementar
  checagens manuais que ele já faz de graça.
- Separe modelos de entrada e de saída quando eles tiverem campos
  diferentes (ex.: senha só entra, nunca é devolvida na resposta).
- Use `/docs` durante o desenvolvimento para testar rapidamente a API
  sem precisar de outra ferramenta.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Introdução ao Flask](../aula-02-introducao-ao-flask/aula.md) · ➡️ [Próxima aula: Persistência com banco de dados: SQLite e ORM](../aula-04-persistencia-com-banco-de-dados-sqlite-orm/aula.md)
