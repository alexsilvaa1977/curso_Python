import pytest

from conta import ContaBancaria


@pytest.fixture
def conta_com_saldo():
    return ContaBancaria("Ana", 100)


def test_saldo_inicial(conta_com_saldo):
    assert conta_com_saldo.saldo == 100


def test_depositar(conta_com_saldo):
    conta_com_saldo.depositar(50)
    assert conta_com_saldo.saldo == 150


def test_sacar(conta_com_saldo):
    conta_com_saldo.sacar(30)
    assert conta_com_saldo.saldo == 70


@pytest.fixture
def arquivo_temporario(tmp_path):
    caminho = tmp_path / "dados.txt"
    caminho.write_text("dados de teste")
    yield str(caminho)
    # tmp_path é limpo automaticamente pelo pytest -- não precisa remover manualmente


def test_leitura_arquivo(arquivo_temporario):
    with open(arquivo_temporario) as f:
        conteudo = f.read()
    assert conteudo == "dados de teste"
