"""Configuração da conexão com o banco de dados (SQLite via SQLAlchemy)."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

CAMINHO_BANCO = os.environ.get("TAREFAS_DB_URL", "sqlite:///tarefas.db")

engine = create_engine(CAMINHO_BANCO, connect_args={"check_same_thread": False})
SessaoLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()


def obter_sessao():
    """Fornece uma sessão de banco de dados para uma requisição, fechando-a ao final."""
    sessao = SessaoLocal()
    try:
        yield sessao
    finally:
        sessao.close()
