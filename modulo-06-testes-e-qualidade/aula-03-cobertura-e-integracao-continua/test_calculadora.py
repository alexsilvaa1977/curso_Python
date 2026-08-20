from calculadora import somar, eh_par


def test_somar():
    assert somar(2, 3) == 5


def test_eh_par_com_numero_par():
    assert eh_par(4) is True


# Nenhum teste chama "dividir()" nem "eh_par()" com um número ímpar --
# de propósito, para o relatório de cobertura mostrar linhas faltando.
