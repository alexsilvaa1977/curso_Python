"""Módulo de exemplo usado pelos testes desta aula.

Simula uma dependência externa (uma chamada de rede) para demonstrar
mocking -- não faz uma requisição de verdade.
"""

import requests


def buscar_temperatura(cidade):
    resposta = requests.get(f"https://api-clima.exemplo/{cidade}")
    return resposta.json()["temperatura"]


def perguntar_nome():
    return input("Qual o seu nome? ")
