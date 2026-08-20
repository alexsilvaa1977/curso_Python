# Aula 4 — Persistência com banco de dados: SQLite e ORM

**Objetivos desta aula:**
- Entender por que uma API real precisa de um banco de dados, não só
  listas em memória.
- Usar SQLAlchemy (um ORM) para modelar e persistir dados em SQLite.
- Integrar a persistência a uma API FastAPI.

## O problema das listas em memória

Nas aulas anteriores, `tarefas` era uma lista Python guardada na
memória do processo. Isso tem duas limitações sérias:

1. **Os dados somem** quando o servidor reinicia (deploy, crash,
   reinício do computador).
2. **Não escala**: se você rodar duas cópias do servidor (comum em
   produção, para lidar com mais tráfego), cada uma teria sua própria
   lista, desincronizada da outra.

A solução é persistir os dados em um **banco de dados**, que existe
independentemente do processo da API.

## SQLite: um banco de dados em arquivo

SQLite é um banco de dados relacional que guarda tudo em um único
arquivo — sem precisar instalar/configurar um servidor de banco de dados
separado. É ótimo para aprender, para aplicações pequenas/médias, e para
testes; projetos com tráfego alto ou múltiplos servidores geralmente
migram para PostgreSQL ou similar (o código muda muito pouco, graças ao
ORM).

## O que é um ORM

*Object-Relational Mapping* — uma camada que permite trabalhar com o
banco de dados usando classes e objetos Python, em vez de escrever SQL
manualmente. SQLAlchemy é o ORM mais usado no ecossistema Python.

## Definindo um modelo com SQLAlchemy

```python
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class TarefaDB(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    concluida = Column(Boolean, default=False)
```

`TarefaDB` descreve uma **tabela** chamada `tarefas`, com três colunas.
Cada instância de `TarefaDB`, depois de salva, corresponde a uma
**linha** dessa tabela.

## Conectando ao banco e criando as tabelas

```python
engine = create_engine("sqlite:///tarefas.db")   # cria/abre o arquivo tarefas.db
Base.metadata.create_all(engine)                    # cria as tabelas, se não existirem

SessaoLocal = sessionmaker(bind=engine)
```

Uma `Session` é o objeto usado para conversar com o banco (adicionar,
buscar, atualizar, remover registros) dentro de uma "unidade de
trabalho".

## Criando (INSERT) e consultando (SELECT)

```python
sessao = SessaoLocal()

nova_tarefa = TarefaDB(titulo="Estudar SQLAlchemy", concluida=False)
sessao.add(nova_tarefa)
sessao.commit()          # grava de fato no arquivo do banco

todas_tarefas = sessao.query(TarefaDB).all()
for tarefa in todas_tarefas:
    print(tarefa.id, tarefa.titulo, tarefa.concluida)
```

```python
tarefa = sessao.query(TarefaDB).filter(TarefaDB.id == 1).first()
print(tarefa.titulo if tarefa else "não encontrada")
```

## Atualizando e removendo

```python
tarefa = sessao.query(TarefaDB).filter(TarefaDB.id == 1).first()
tarefa.concluida = True
sessao.commit()             # a mudança no objeto é sincronizada com o banco
```

```python
tarefa = sessao.query(TarefaDB).filter(TarefaDB.id == 1).first()
sessao.delete(tarefa)
sessao.commit()
```

## Integrando com FastAPI

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

def obter_sessao():
    sessao = SessaoLocal()
    try:
        yield sessao       # entrega a sessão para a rota usar
    finally:
        sessao.close()      # sempre fecha, mesmo se a rota falhar

@app.get("/tarefas")
def listar_tarefas(sessao: Session = Depends(obter_sessao)):
    return sessao.query(TarefaDB).all()

@app.post("/tarefas", status_code=201)
def criar_tarefa(nova_tarefa: NovaTarefa, sessao: Session = Depends(obter_sessao)):
    tarefa = TarefaDB(titulo=nova_tarefa.titulo, concluida=nova_tarefa.concluida)
    sessao.add(tarefa)
    sessao.commit()
    sessao.refresh(tarefa)     # atualiza "tarefa" com o id gerado pelo banco
    return tarefa
```

`Depends(obter_sessao)` é o sistema de **injeção de dependências** do
FastAPI: ele chama `obter_sessao()` para cada requisição, entrega a
sessão à rota, e garante que ela é fechada ao final — mesmo que a rota
levante uma exceção.

## Banco de dados em memória para testes

Testes automatizados (módulo 6) não devem depender do arquivo real de
produção. Um banco SQLite em memória (`sqlite:///:memory:`) existe só
durante a execução do teste, e desaparece completamente ao final:

```python
from sqlalchemy.pool import StaticPool

engine_teste = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,   # mantém a mesma conexão em memória entre as sessões do teste
)
Base.metadata.create_all(engine_teste)
SessaoTeste = sessionmaker(bind=engine_teste)
```

O `poolclass=StaticPool` é importante: sem ele, cada nova sessão abriria
uma conexão **separada** ao banco em memória, e como cada conexão
`:memory:` é isolada por padrão, as tabelas criadas por `create_all`
"desapareceriam" para qualquer sessão seguinte (erro
`no such table`). `StaticPool` garante que todas as sessões do teste
compartilhem a mesma conexão/banco em memória.

## Erros comuns

- Esquecer `sessao.commit()` — sem ele, as mudanças ficam pendentes na
  sessão e nunca chegam a ser gravadas no arquivo do banco.
- Esquecer `sessao.close()` (ou não usar `Depends` com `yield`, que
  fecha automaticamente) — sessões abertas demais podem esgotar
  conexões disponíveis.
- Rodar os testes contra o banco de dados de produção — sempre use um
  banco separado (em memória ou um arquivo `.db` só para testes).

## Boas práticas

- Use `Depends` com `yield` para gerenciar o ciclo de vida da sessão
  automaticamente em cada rota do FastAPI.
- Separe o banco usado em testes do banco usado em desenvolvimento/
  produção — nunca testes rodando contra dados reais.
- Trate o "não encontrado" (`sessao.query(...).first()` retornando
  `None`) explicitamente, devolvendo `404` em vez de deixar o código
  quebrar com `AttributeError`.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Introdução ao FastAPI](../aula-03-introducao-ao-fastapi/aula.md) · ➡️ [Próximo módulo: Projeto final](../../modulo-09-projeto-final/README.md)
