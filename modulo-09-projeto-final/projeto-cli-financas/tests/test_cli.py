from src.cli import executar


def test_adicionar_e_listar(tmp_path, capsys):
    caminho = str(tmp_path / "financas.json")

    codigo = executar(["--arquivo", caminho, "adicionar", "Salário", "3000", "--categoria", "renda"])
    assert codigo == 0

    executar(["--arquivo", caminho, "listar"])
    saida = capsys.readouterr().out
    assert "Salário" in saida
    assert "renda" in saida


def test_adicionar_com_valor_zero_retorna_erro(tmp_path, capsys):
    caminho = str(tmp_path / "financas.json")

    codigo = executar(["--arquivo", caminho, "adicionar", "Inválida", "0"])
    assert codigo == 1
    assert "Erro" in capsys.readouterr().err


def test_saldo_apos_varias_transacoes(tmp_path, capsys):
    caminho = str(tmp_path / "financas.json")

    executar(["--arquivo", caminho, "adicionar", "Salário", "3000"])
    executar(["--arquivo", caminho, "adicionar", "Aluguel", "-1200"])

    executar(["--arquivo", caminho, "saldo"])
    saida = capsys.readouterr().out
    assert "1800.00" in saida


def test_remover_transacao_inexistente_retorna_erro(tmp_path, capsys):
    caminho = str(tmp_path / "financas.json")

    codigo = executar(["--arquivo", caminho, "remover", "999"])
    assert codigo == 1
    assert "Erro" in capsys.readouterr().err


def test_dados_persistem_entre_execucoes(tmp_path, capsys):
    caminho = str(tmp_path / "financas.json")

    executar(["--arquivo", caminho, "adicionar", "Salário", "3000"])
    # Uma nova chamada a "executar" simula uma nova execução do programa,
    # que precisa carregar o que foi salvo na chamada anterior.
    executar(["--arquivo", caminho, "listar"])

    saida = capsys.readouterr().out
    assert "Salário" in saida
