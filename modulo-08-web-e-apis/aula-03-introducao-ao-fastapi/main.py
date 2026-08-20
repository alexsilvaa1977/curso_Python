"""API de tarefas de exemplo usada nesta aula, construída com FastAPI."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool = False


class NovaTarefa(BaseModel):
    titulo: str
    concluida: bool = False


tarefas = [Tarefa(id=1, titulo="Estudar Python", concluida=False)]


@app.get("/tarefas")
def listar_tarefas():
    return tarefas


@app.get("/tarefas/{id_tarefa}")
def buscar_tarefa(id_tarefa: int):
    for tarefa in tarefas:
        if tarefa.id == id_tarefa:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")


@app.post("/tarefas", status_code=201)
def criar_tarefa(nova_tarefa: NovaTarefa):
    novo_id = max((t.id for t in tarefas), default=0) + 1
    tarefa = Tarefa(id=novo_id, titulo=nova_tarefa.titulo, concluida=nova_tarefa.concluida)
    tarefas.append(tarefa)
    return tarefa


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
