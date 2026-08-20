from fastapi.testclient import TestClient

from main import app

cliente = TestClient(app)


def test_listar_tarefas():
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)


def test_buscar_tarefa_inexistente():
    resposta = cliente.get("/tarefas/999")
    assert resposta.status_code == 404


def test_buscar_tarefa_com_id_invalido():
    resposta = cliente.get("/tarefas/abc")
    assert resposta.status_code == 422


def test_criar_tarefa():
    resposta = cliente.post("/tarefas", json={"titulo": "Nova tarefa"})
    assert resposta.status_code == 201
    assert resposta.json()["titulo"] == "Nova tarefa"


def test_criar_tarefa_sem_titulo_falha_validacao():
    resposta = cliente.post("/tarefas", json={})
    assert resposta.status_code == 422


def test_atualizar_tarefa():
    resposta = cliente.put("/tarefas/1", json={"titulo": "Estudar Python", "concluida": True})
    assert resposta.status_code == 200
    assert resposta.json()["concluida"] is True


def test_remover_tarefa():
    resposta_criacao = cliente.post("/tarefas", json={"titulo": "Tarefa temporária"})
    id_criado = resposta_criacao.json()["id"]

    resposta_remocao = cliente.delete(f"/tarefas/{id_criado}")
    assert resposta_remocao.status_code == 204

    resposta_busca = cliente.get(f"/tarefas/{id_criado}")
    assert resposta_busca.status_code == 404
