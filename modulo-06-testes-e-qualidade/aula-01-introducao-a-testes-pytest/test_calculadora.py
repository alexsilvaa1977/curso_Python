import pytest

from calculadora import somar, dividir


def test_somar_numeros_positivos():
    assert somar(2, 3) == 5


def test_somar_numeros_negativos():
    assert somar(-2, -3) == -5


def test_somar_com_zero():
    assert somar(5, 0) == 5


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_zero_levanta_erro():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
