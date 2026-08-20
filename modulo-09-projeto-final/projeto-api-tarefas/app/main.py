"""Ponto de entrada da API: define as rotas HTTP e conecta tudo (banco,
schemas, funções de CRUD).

Para rodar localmente:
    uvicorn app.main:app --reload
Depois acesse http://127.0.0.1:8000/docs para a documentação interativa.
"""

from fastapi import Depends, FastAPI, HTTPException

from app import crud
from app.database import Base, engine, obter_sessao
from app.schemas import TarefaAtualizacao, TarefaEntrada, TarefaSaida
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

app = FastAPI(
    title="API de Tarefas",
    description="Projeto final do curso de Python — CRUD de tarefas com FastAPI e SQLAlchemy.",
)


@app.get("/tarefas", response_model=list[TarefaSaida])
def listar_tarefas(
    apenas_pendentes: bool = False, sessao: Session = Depends(obter_sessao)
):
    return crud.listar_tarefas(sessao, apenas_pendentes=apenas_pendentes)


@app.get("/tarefas/contagem")
def contar_tarefas(sessao: Session = Depends(obter_sessao)):
    return crud.contar_tarefas(sessao)


@app.get("/tarefas/{id_tarefa}", response_model=TarefaSaida)
def buscar_tarefa(id_tarefa: int, sessao: Session = Depends(obter_sessao)):
    tarefa = crud.buscar_tarefa(sessao, id_tarefa)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


@app.post("/tarefas", response_model=TarefaSaida, status_code=201)
def criar_tarefa(dados: TarefaEntrada, sessao: Session = Depends(obter_sessao)):
    return crud.criar_tarefa(sessao, dados)


@app.put("/tarefas/{id_tarefa}", response_model=TarefaSaida)
def atualizar_tarefa(
    id_tarefa: int, dados: TarefaAtualizacao, sessao: Session = Depends(obter_sessao)
):
    tarefa = crud.buscar_tarefa(sessao, id_tarefa)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return crud.atualizar_tarefa(sessao, tarefa, dados)


@app.delete("/tarefas/{id_tarefa}", status_code=204)
def remover_tarefa(id_tarefa: int, sessao: Session = Depends(obter_sessao)):
    tarefa = crud.buscar_tarefa(sessao, id_tarefa)
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    crud.remover_tarefa(sessao, tarefa)
