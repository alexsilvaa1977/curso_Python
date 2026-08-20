"""Modelos de banco de dados (tabelas) do projeto."""

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    concluida = Column(Boolean, default=False, nullable=False)
    criada_em = Column(DateTime, server_default=func.now())
