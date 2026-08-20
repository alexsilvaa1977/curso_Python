from app import app


def test_pagina_inicial():
    cliente = app.test_client()
    resposta = cliente.get("/")
    assert resposta.status_code == 200


def test_listar_tarefas():
    cliente = app.test_client()
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200
    assert isinstance(resposta.get_json(), list)


def test_buscar_tarefa_inexistente():
    cliente = app.test_client()
    resposta = cliente.get("/tarefas/999")
    assert resposta.status_code == 404


def test_criar_tarefa():
    cliente = app.test_client()
    resposta = cliente.post("/tarefas", json={"titulo": "Nova tarefa"})
    assert resposta.status_code == 201
    assert resposta.get_json()["titulo"] == "Nova tarefa"


def test_atualizar_tarefa():
    cliente = app.test_client()
    resposta = cliente.put("/tarefas/1", json={"concluida": True})
    assert resposta.status_code == 200
    assert resposta.get_json()["concluida"] is True


def test_remover_tarefa():
    cliente = app.test_client()
    resposta_criacao = cliente.post("/tarefas", json={"titulo": "Tarefa temporária"})
    id_criado = resposta_criacao.get_json()["id"]

    resposta_remocao = cliente.delete(f"/tarefas/{id_criado}")
    assert resposta_remocao.status_code == 204

    resposta_busca = cliente.get(f"/tarefas/{id_criado}")
    assert resposta_busca.status_code == 404
