"""Camada de persistência: salva e carrega as transações de um arquivo
JSON (módulo 5 do curso).
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from src.dominio import Carteira, Transacao


def salvar(carteira: Carteira, caminho: str | Path) -> None:
    dados = [
        {
            "id": t.id,
            "descricao": t.descricao,
            "valor": t.valor,
            "categoria": t.categoria,
            "data": t.data.isoformat(),
        }
        for t in carteira.listar()
    ]
    Path(caminho).write_text(
        json.dumps(dados, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def carregar(caminho: str | Path) -> Carteira:
    caminho = Path(caminho)
    carteira = Carteira()

    if not caminho.exists():
        return carteira

    conteudo = caminho.read_text(encoding="utf-8").strip()
    if not conteudo:
        return carteira

    dados = json.loads(conteudo)
    transacoes = [
        Transacao(
            id=item["id"],
            descricao=item["descricao"],
            valor=item["valor"],
            categoria=item["categoria"],
            data=date.fromisoformat(item["data"]),
        )
        for item in dados
    ]
    carteira.carregar_transacoes(transacoes)
    return carteira
