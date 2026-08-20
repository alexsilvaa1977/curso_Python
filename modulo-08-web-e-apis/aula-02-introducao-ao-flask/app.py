"""API de tarefas de exemplo usada nesta aula, construída com Flask."""

from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Estudar Python", "concluida": False},
]


@app.route("/")
def pagina_inicial():
    return "API de tarefas no ar!"


@app.route("/tarefas")
def listar_tarefas():
    return jsonify(tarefas)


@app.route("/tarefas/<int:id_tarefa>")
def buscar_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()
    novo_id = max((t["id"] for t in tarefas), default=0) + 1
    nova_tarefa = {"id": novo_id, "titulo": dados["titulo"], "concluida": False}
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


@app.route("/tarefas/<int:id_tarefa>", methods=["PUT"])
def atualizar_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            dados = request.get_json()
            tarefa["titulo"] = dados.get("titulo", tarefa["titulo"])
            tarefa["concluida"] = dados.get("concluida", tarefa["concluida"])
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404


@app.route("/tarefas/<int:id_tarefa>", methods=["DELETE"])
def remover_tarefa(id_tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t["id"] != id_tarefa]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
