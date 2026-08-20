"""API de tarefas de exemplo usada nesta aula, com persistência em
SQLite via SQLAlchemy, integrada ao FastAPI.
"""

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

Base = declarative_base()


class TarefaDB(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    concluida = Column(Boolean, default=False)


engine = create_engine("sqlite:///tarefas.db", connect_args={"check_same_thread": False})
Base.metadata.create_all(engine)
SessaoLocal = sessionmaker(bind=engine)


def obter_sessao():
    sessao = SessaoLocal()
    try:
        yield sessao
    finally:
        sessao.close()


class NovaTarefa(BaseModel):
    titulo: str
    concluida: bool = False


app = FastAPI()


@app.get("/tarefas")
def listar_tarefas(sessao: Session = Depends(obter_sessao)):
    return sessao.query(TarefaDB).all()


@app.get("/tarefas/{id_tarefa}")
def buscar_tarefa(id_tarefa: int, sessao: Session = Depends(obter_sessao)):
    tarefa = sessao.query(TarefaDB).filter(TarefaDB.id == id_tarefa).first()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


@app.post("/tarefas", status_code=201)
def criar_tarefa(nova_tarefa: NovaTarefa, sessao: Session = Depends(obter_sessao)):
    tarefa = TarefaDB(titulo=nova_tarefa.titulo, concluida=nova_tarefa.concluida)
    sessao.add(tarefa)
    sessao.commit()
    sessao.refresh(tarefa)
    return tarefa


@app.put("/tarefas/{id_tarefa}")
def atualizar_tarefa(
    id_tarefa: int, dados: NovaTarefa, sessao: Session = Depends(obter_sessao)
):
    tarefa = sessao.query(TarefaDB).filter(TarefaDB.id == id_tarefa).first()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa.titulo = dados.titulo
    tarefa.concluida = dados.concluida
    sessao.commit()
    sessao.refresh(tarefa)
    return tarefa


@app.delete("/tarefas/{id_tarefa}", status_code=204)
def remover_tarefa(id_tarefa: int, sessao: Session = Depends(obter_sessao)):
    tarefa = sessao.query(TarefaDB).filter(TarefaDB.id == id_tarefa).first()
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    sessao.delete(tarefa)
    sessao.commit()
