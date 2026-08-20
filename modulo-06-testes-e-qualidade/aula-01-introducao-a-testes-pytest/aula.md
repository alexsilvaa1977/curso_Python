# Aula 1 — Introdução a testes com pytest

**Objetivos desta aula:**
- Entender por que testes automatizados importam.
- Escrever testes simples com `assert` e a convenção do `pytest`.
- Rodar testes pela linha de comando e interpretar o resultado.
- Testar que uma exceção é levantada com `pytest.raises`.

## Por que testar

Até aqui, você verificou se o código funciona rodando-o manualmente e
olhando a saída. Isso funciona para scripts pequenos, mas não escala:
conforme o projeto cresce, é fácil uma mudança "quebrar" uma parte que
você não lembrou de testar de novo manualmente.

Um **teste automatizado** é um pequeno programa que verifica se outro
trecho de código se comporta como esperado — e pode ser rodado a
qualquer momento, em segundos, para todo o projeto.

## `assert`: a base de qualquer teste

```python
def somar(a, b):
    return a + b

assert somar(2, 3) == 5          # se for verdade, nada acontece
assert somar(2, 3) == 10          # ERRO: AssertionError
```

`assert condicao` não faz nada se `condicao` for verdadeira; levanta
`AssertionError` se for falsa. É o mecanismo básico por trás de qualquer
framework de testes.

## `pytest`: convenção e primeiro teste

`pytest` é a ferramenta de testes mais usada no ecossistema Python
(já está no `requirements.txt` deste curso). Ele segue convenções de
nomenclatura para **descobrir** os testes automaticamente:

- Arquivos de teste começam com `test_` (ex.: `test_calculadora.py`).
- Funções de teste começam com `test_` (ex.: `def test_soma():`).

```python
# arquivo: calculadora.py
def somar(a, b):
    return a + b

def dividir(a, b):
    return a / b
```

```python
# arquivo: test_calculadora.py
from calculadora import somar, dividir

def test_somar_numeros_positivos():
    assert somar(2, 3) == 5

def test_somar_com_zero():
    assert somar(5, 0) == 5

def test_dividir():
    assert dividir(10, 2) == 5
```

Rodando no terminal, na pasta com os dois arquivos:

```bash
pytest
```

Saída (resumida):
```
collected 3 items

test_calculadora.py ...                                       [100%]

3 passed in 0.01s
```

Cada `.` representa um teste que passou. Se um teste falhar, o `pytest`
mostra exatamente qual `assert` falhou e os valores envolvidos —
bem mais detalhado do que um `assert` isolado no seu próprio script.

## Um teste que falha (para entender a saída)

```python
def test_dividir_errado():
    assert dividir(10, 2) == 6     # errado de propósito
```

```
FAILED test_calculadora.py::test_dividir_errado - assert 5.0 == 6
```

O `pytest` mostra o valor **real** (`5.0`) e o valor **esperado** pelo
teste (`6`), facilitando identificar o problema.

## Testando exceções com `pytest.raises`

Como testar que uma função **levanta** uma exceção quando deveria
(relembrando exceções, módulo 5)?

```python
import pytest
from calculadora import dividir

def test_dividir_por_zero_levanta_erro():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
```

Se `dividir(10, 0)` **não** levantar `ZeroDivisionError`, o teste falha
— `pytest.raises` verifica que a exceção esperada realmente aconteceu.

## Organizando múltiplos testes

Um arquivo de teste pode (e deve) ter vários testes pequenos, cada um
verificando **um** comportamento específico — nomes descritivos ajudam a
entender o que quebrou só de olhar o nome do teste que falhou:

```python
def test_somar_numeros_positivos():
    assert somar(2, 3) == 5

def test_somar_numeros_negativos():
    assert somar(-2, -3) == -5

def test_somar_positivo_com_negativo():
    assert somar(5, -3) == 2
```

## Erros comuns

- Nomear o arquivo ou a função de teste sem o prefixo `test_` — o
  `pytest` simplesmente não encontra e não executa esse teste, sem
  avisar que ele foi "esquecido".
- Escrever um teste que verifica várias coisas não relacionadas de uma
  vez — se falhar, fica difícil saber qual parte especificamente quebrou.
  Prefira testes pequenos e focados.
- Escrever testes que dependem da ordem de execução um do outro — cada
  teste deve funcionar de forma independente, em qualquer ordem.

## Boas práticas

- Um teste por comportamento, com nome descritivo
  (`test_dividir_por_zero_levanta_erro`, não `test_1`).
- Sempre inclua ao menos um teste para o "caminho feliz" (entrada
  normal) e um para o caso de erro esperado.
- Rode `pytest` com frequência durante o desenvolvimento, não só no
  final — quanto mais rápido você descobre que quebrou algo, mais fácil
  é corrigir.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Voltar ao índice do módulo](../README.md) · ➡️ [Próxima aula: Fixtures e mocks](../aula-02-fixtures-e-mocks/aula.md)
