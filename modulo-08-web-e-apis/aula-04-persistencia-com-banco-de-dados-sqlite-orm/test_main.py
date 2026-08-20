from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from main import Base, app, obter_sessao

engine_teste = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # mantém a mesma conexão em memória entre as sessões do teste
)
Base.metadata.create_all(engine_teste)
SessaoTeste = sessionmaker(bind=engine_teste)


def obter_sessao_teste():
    sessao = SessaoTeste()
    try:
        yield sessao
    finally:
        sessao.close()


app.dependency_overrides[obter_sessao] = obter_sessao_teste

cliente = TestClient(app)


def test_listar_tarefas_vazio():
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200
    assert resposta.json() == []


def test_criar_e_buscar_tarefa():
    resposta_criacao = cliente.post("/tarefas", json={"titulo": "Estudar SQLAlchemy"})
    assert resposta_criacao.status_code == 201
    id_criado = resposta_criacao.json()["id"]

    resposta_busca = cliente.get(f"/tarefas/{id_criado}")
    assert resposta_busca.status_code == 200
    assert resposta_busca.json()["titulo"] == "Estudar SQLAlchemy"


def test_buscar_tarefa_inexistente():
    resposta = cliente.get("/tarefas/999")
    assert resposta.status_code == 404


def test_atualizar_tarefa():
    resposta_criacao = cliente.post("/tarefas", json={"titulo": "Antes"})
    id_criado = resposta_criacao.json()["id"]

    resposta_atualizacao = cliente.put(
        f"/tarefas/{id_criado}", json={"titulo": "Depois", "concluida": True}
    )
    assert resposta_atualizacao.status_code == 200
    assert resposta_atualizacao.json()["titulo"] == "Depois"
    assert resposta_atualizacao.json()["concluida"] is True


def test_remover_tarefa():
    resposta_criacao = cliente.post("/tarefas", json={"titulo": "Tarefa temporária"})
    id_criado = resposta_criacao.json()["id"]

    resposta_remocao = cliente.delete(f"/tarefas/{id_criado}")
    assert resposta_remocao.status_code == 204

    resposta_busca = cliente.get(f"/tarefas/{id_criado}")
    assert resposta_busca.status_code == 404
