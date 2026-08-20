from datetime import date

import pytest

from src.dominio import (
    Carteira,
    Transacao,
    TransacaoNaoEncontradaError,
    ValorInvalidoError,
)


def test_criar_transacao_valida():
    transacao = Transacao(id=1, descricao="Salário", valor=3000)
    assert transacao.eh_receita is True


def test_criar_transacao_com_valor_zero_levanta_erro():
    with pytest.raises(ValorInvalidoError):
        Transacao(id=1, descricao="Inválida", valor=0)


def test_carteira_comeca_vazia():
    carteira = Carteira()
    assert len(carteira) == 0
    assert carteira.saldo() == 0


def test_adicionar_gera_ids_sequenciais():
    carteira = Carteira()
    t1 = carteira.adicionar("A", 100)
    t2 = carteira.adicionar("B", -50)
    assert t1.id == 1
    assert t2.id == 2


def test_saldo_soma_receitas_e_despesas():
    carteira = Carteira()
    carteira.adicionar("Salário", 3000)
    carteira.adicionar("Aluguel", -1200)
    carteira.adicionar("Mercado", -300)
    assert carteira.saldo() == 1500
    assert carteira.total_receitas() == 3000
    assert carteira.total_despesas() == -1500


def test_listar_filtra_por_categoria():
    carteira = Carteira()
    carteira.adicionar("Salário", 3000, categoria="renda")
    carteira.adicionar("Aluguel", -1200, categoria="moradia")

    resultado = carteira.listar(categoria="moradia")
    assert len(resultado) == 1
    assert resultado[0].descricao == "Aluguel"


def test_listar_ordena_por_data():
    carteira = Carteira()
    carteira.adicionar("Mais recente", 100, data=date(2024, 6, 1))
    carteira.adicionar("Mais antiga", 50, data=date(2024, 1, 1))

    resultado = carteira.listar()
    assert resultado[0].descricao == "Mais antiga"
    assert resultado[1].descricao == "Mais recente"


def test_remover_transacao_existente():
    carteira = Carteira()
    transacao = carteira.adicionar("Temporária", 10)
    carteira.remover(transacao.id)
    assert len(carteira) == 0


def test_remover_transacao_inexistente_levanta_erro():
    carteira = Carteira()
    with pytest.raises(TransacaoNaoEncontradaError):
        carteira.remover(999)


def test_buscar_transacao_existente():
    carteira = Carteira()
    transacao = carteira.adicionar("Salário", 3000)
    encontrada = carteira.buscar(transacao.id)
    assert encontrada is transacao


def test_carregar_transacoes_ajusta_proximo_id():
    carteira = Carteira()
    carteira.carregar_transacoes(
        [Transacao(id=5, descricao="Antiga", valor=100)]
    )
    nova = carteira.adicionar("Nova", 50)
    assert nova.id == 6
