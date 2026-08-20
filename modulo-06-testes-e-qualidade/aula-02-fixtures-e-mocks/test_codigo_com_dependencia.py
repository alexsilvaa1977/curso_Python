from unittest.mock import Mock

import codigo_com_dependencia
from codigo_com_dependencia import buscar_temperatura, perguntar_nome


def test_buscar_temperatura(monkeypatch):
    resposta_falsa = Mock()
    resposta_falsa.json.return_value = {"temperatura": 25}

    def get_falso(url):
        return resposta_falsa

    monkeypatch.setattr(codigo_com_dependencia.requests, "get", get_falso)

    resultado = buscar_temperatura("Recife")
    assert resultado == 25


def test_perguntar_nome(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt="": "Ana")
    assert perguntar_nome() == "Ana"
