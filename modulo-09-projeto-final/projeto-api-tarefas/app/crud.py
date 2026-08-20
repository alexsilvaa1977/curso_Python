"""Funções de acesso a dados (Create, Read, Update, Delete) para tarefas.

Manter essas funções separadas das rotas facilita testá-las
isoladamente e reaproveitá-las (por exemplo, em um script de
administração que não passa pela API HTTP).
"""

from sqlalchemy.orm import Session

from app.models import Tarefa
from app.schemas import TarefaAtualizacao, TarefaEntrada


def listar_tarefas(sessao: Session, apenas_pendentes: bool = False) -> list[Tarefa]:
    consulta = sessao.query(Tarefa)
    if apenas_pendentes:
        consulta = consulta.filter(Tarefa.concluida.is_(False))
    return consulta.order_by(Tarefa.id).all()


def buscar_tarefa(sessao: Session, id_tarefa: int) -> Tarefa | None:
    return sessao.query(Tarefa).filter(Tarefa.id == id_tarefa).first()


def criar_tarefa(sessao: Session, dados: TarefaEntrada) -> Tarefa:
    tarefa = Tarefa(
        titulo=dados.titulo, descricao=dados.descricao, concluida=dados.concluida
    )
    sessao.add(tarefa)
    sessao.commit()
    sessao.refresh(tarefa)
    return tarefa


def atualizar_tarefa(
    sessao: Session, tarefa: Tarefa, dados: TarefaAtualizacao
) -> Tarefa:
    dados_informados = dados.model_dump(exclude_unset=True)
    for campo, valor in dados_informados.items():
        setattr(tarefa, campo, valor)
    sessao.commit()
    sessao.refresh(tarefa)
    return tarefa


def remover_tarefa(sessao: Session, tarefa: Tarefa) -> None:
    sessao.delete(tarefa)
    sessao.commit()


def contar_tarefas(sessao: Session) -> dict[str, int]:
    total = sessao.query(Tarefa).count()
    concluidas = sessao.query(Tarefa).filter(Tarefa.concluida.is_(True)).count()
    return {"total": total, "concluidas": concluidas, "pendentes": total - concluidas}
