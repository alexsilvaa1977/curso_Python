def test_lista_comeca_vazia(cliente):
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == 200
    assert resposta.json() == []


def test_criar_tarefa(cliente):
    resposta = cliente.post("/tarefas", json={"titulo": "Estudar FastAPI"})
    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["titulo"] == "Estudar FastAPI"
    assert corpo["concluida"] is False
    assert corpo["id"] is not None


def test_criar_tarefa_com_titulo_vazio_falha_validacao(cliente):
    resposta = cliente.post("/tarefas", json={"titulo": "   "})
    assert resposta.status_code == 422


def test_criar_tarefa_sem_titulo_falha_validacao(cliente):
    resposta = cliente.post("/tarefas", json={})
    assert resposta.status_code == 422


def test_buscar_tarefa_existente(cliente):
    id_criado = cliente.post("/tarefas", json={"titulo": "Ler documentação"}).json()["id"]
    resposta = cliente.get(f"/tarefas/{id_criado}")
    assert resposta.status_code == 200
    assert resposta.json()["titulo"] == "Ler documentação"


def test_buscar_tarefa_inexistente(cliente):
    resposta = cliente.get("/tarefas/999")
    assert resposta.status_code == 404


def test_atualizar_tarefa_parcialmente(cliente):
    id_criado = cliente.post("/tarefas", json={"titulo": "Rascunho"}).json()["id"]

    resposta = cliente.put(f"/tarefas/{id_criado}", json={"concluida": True})
    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["concluida"] is True
    assert corpo["titulo"] == "Rascunho"  # não foi alterado, pois não foi enviado


def test_atualizar_tarefa_inexistente(cliente):
    resposta = cliente.put("/tarefas/999", json={"concluida": True})
    assert resposta.status_code == 404


def test_remover_tarefa(cliente):
    id_criado = cliente.post("/tarefas", json={"titulo": "Tarefa temporária"}).json()["id"]

    resposta_remocao = cliente.delete(f"/tarefas/{id_criado}")
    assert resposta_remocao.status_code == 204

    resposta_busca = cliente.get(f"/tarefas/{id_criado}")
    assert resposta_busca.status_code == 404


def test_remover_tarefa_inexistente(cliente):
    resposta = cliente.delete("/tarefas/999")
    assert resposta.status_code == 404


def test_listar_apenas_pendentes(cliente):
    id_a = cliente.post("/tarefas", json={"titulo": "A"}).json()["id"]
    cliente.post("/tarefas", json={"titulo": "B", "concluida": True})

    resposta = cliente.get("/tarefas", params={"apenas_pendentes": True})
    tarefas = resposta.json()
    assert len(tarefas) == 1
    assert tarefas[0]["id"] == id_a


def test_contagem_de_tarefas(cliente):
    cliente.post("/tarefas", json={"titulo": "A"})
    cliente.post("/tarefas", json={"titulo": "B", "concluida": True})
    cliente.post("/tarefas", json={"titulo": "C", "concluida": True})

    resposta = cliente.get("/tarefas/contagem")
    assert resposta.json() == {"total": 3, "concluidas": 2, "pendentes": 1}
