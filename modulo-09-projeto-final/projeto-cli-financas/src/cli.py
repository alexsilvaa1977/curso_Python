"""Interface de linha de comando do controle financeiro pessoal.

Uso:
    python3 -m src.cli adicionar "Salário" 3000 --categoria renda
    python3 -m src.cli adicionar "Aluguel" -1200 --categoria moradia
    python3 -m src.cli listar
    python3 -m src.cli listar --categoria moradia
    python3 -m src.cli saldo
    python3 -m src.cli remover 2
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

from src.dominio import TransacaoNaoEncontradaError, ValorInvalidoError
from src.persistencia import carregar, salvar

CAMINHO_PADRAO = Path("financas.json")


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="financas", description="Controle financeiro pessoal via linha de comando."
    )
    parser.add_argument(
        "--arquivo",
        default=str(CAMINHO_PADRAO),
        help="Caminho do arquivo JSON de dados (padrão: financas.json)",
    )

    subcomandos = parser.add_subparsers(dest="comando", required=True)

    parser_adicionar = subcomandos.add_parser("adicionar", help="Adiciona uma transação")
    parser_adicionar.add_argument("descricao")
    parser_adicionar.add_argument("valor", type=float, help="Positivo = receita, negativo = despesa")
    parser_adicionar.add_argument("--categoria", default="geral")
    parser_adicionar.add_argument("--data", help="Data no formato AAAA-MM-DD (padrão: hoje)")

    parser_listar = subcomandos.add_parser("listar", help="Lista transações")
    parser_listar.add_argument("--categoria", default=None)

    subcomandos.add_parser("saldo", help="Exibe o saldo atual (receitas - despesas)")

    parser_remover = subcomandos.add_parser("remover", help="Remove uma transação pelo id")
    parser_remover.add_argument("id", type=int)

    return parser


def executar(argv: list[str] | None = None) -> int:
    parser = construir_parser()
    args = parser.parse_args(argv)
    carteira = carregar(args.arquivo)

    if args.comando == "adicionar":
        try:
            data_transacao = date.fromisoformat(args.data) if args.data else None
            transacao = carteira.adicionar(
                descricao=args.descricao,
                valor=args.valor,
                categoria=args.categoria,
                data=data_transacao,
            )
        except ValorInvalidoError as erro:
            print(f"Erro: {erro}", file=sys.stderr)
            return 1
        print(f"Transação adicionada: {transacao}")

    elif args.comando == "listar":
        transacoes = carteira.listar(categoria=args.categoria)
        if not transacoes:
            print("Nenhuma transação encontrada.")
        for transacao in transacoes:
            print(transacao)

    elif args.comando == "saldo":
        print(f"Receitas:  R$ {carteira.total_receitas():.2f}")
        print(f"Despesas:  R$ {carteira.total_despesas():.2f}")
        print(f"Saldo:     R$ {carteira.saldo():.2f}")

    elif args.comando == "remover":
        try:
            carteira.remover(args.id)
        except TransacaoNaoEncontradaError as erro:
            print(f"Erro: {erro}", file=sys.stderr)
            return 1
        print(f"Transação #{args.id} removida.")

    salvar(carteira, args.arquivo)
    return 0


if __name__ == "__main__":
    sys.exit(executar())
