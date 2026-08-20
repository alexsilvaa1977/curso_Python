import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, obter_sessao
from app.main import app

engine_teste = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
SessaoTeste = sessionmaker(bind=engine_teste, autoflush=False)


def _obter_sessao_teste():
    sessao = SessaoTeste()
    try:
        yield sessao
    finally:
        sessao.close()


app.dependency_overrides[obter_sessao] = _obter_sessao_teste


@pytest.fixture(autouse=True)
def banco_limpo():
    """Recria as tabelas antes de cada teste, garantindo isolamento entre eles."""
    Base.metadata.drop_all(engine_teste)
    Base.metadata.create_all(engine_teste)
    yield


@pytest.fixture
def cliente():
    return TestClient(app)
