from datetime import date

from src.dominio import Carteira
from src.persistencia import carregar, salvar


def test_salvar_e_carregar_preserva_transacoes(tmp_path):
    caminho = tmp_path / "financas.json"

    carteira_original = Carteira()
    carteira_original.adicionar("Salário", 3000, categoria="renda", data=date(2024, 1, 5))
    carteira_original.adicionar("Aluguel", -1200, categoria="moradia", data=date(2024, 1, 10))

    salvar(carteira_original, caminho)
    carteira_carregada = carregar(caminho)

    assert len(carteira_carregada) == 2
    assert carteira_carregada.saldo() == carteira_original.saldo()

    transacao = carteira_carregada.buscar(1)
    assert transacao.descricao == "Salário"
    assert transacao.categoria == "renda"
    assert transacao.data == date(2024, 1, 5)


def test_carregar_arquivo_inexistente_retorna_carteira_vazia(tmp_path):
    caminho = tmp_path / "nao_existe.json"
    carteira = carregar(caminho)
    assert len(carteira) == 0


def test_carregar_preserva_proximo_id_para_novas_transacoes(tmp_path):
    caminho = tmp_path / "financas.json"

    carteira_original = Carteira()
    carteira_original.adicionar("Primeira", 100)
    carteira_original.remover(1)
    carteira_original.adicionar("Segunda", 200)  # deve ficar com id 2
    salvar(carteira_original, caminho)

    carteira_carregada = carregar(caminho)
    nova = carteira_carregada.adicionar("Terceira", 300)
    assert nova.id == 3
