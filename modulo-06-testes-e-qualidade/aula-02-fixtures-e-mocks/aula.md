# Aula 2 — Fixtures e mocks

**Objetivos desta aula:**
- Usar `@pytest.fixture` para reaproveitar setup entre testes.
- Entender o que é um mock e por que usá-lo.
- Usar `monkeypatch` para substituir comportamento durante o teste.

## O problema: setup repetido

Muitos testes precisam de um mesmo objeto/estado inicial. Sem fixtures,
isso significa repetir o mesmo código de preparação em cada teste:

```python
def test_saldo_inicial():
    conta = ContaBancaria("Ana", 100)
    assert conta.saldo == 100

def test_depositar():
    conta = ContaBancaria("Ana", 100)   # repetido
    conta.depositar(50)
    assert conta.saldo == 150

def test_sacar():
    conta = ContaBancaria("Ana", 100)   # repetido de novo
    conta.sacar(30)
    assert conta.saldo == 70
```

## `@pytest.fixture`: preparando dados uma vez, reusando em vários testes

```python
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
```

Cada teste que recebe `conta_com_saldo` como parâmetro ganha uma
instância **nova** — o `pytest` chama a fixture de novo para cada teste,
evitando que um teste "contamine" o estado usado por outro.

## Fixtures com `setup` e `teardown` (usando `yield`)

Quando é preciso "limpar" algo depois do teste (fechar um arquivo,
remover dados temporários), use `yield` na fixture:

```python
import pytest
import tempfile
import os

@pytest.fixture
def arquivo_temporario():
    caminho = tempfile.mktemp()
    with open(caminho, "w") as f:
        f.write("dados de teste")
    yield caminho          # o teste roda aqui, recebendo "caminho"
    os.remove(caminho)      # executado depois do teste, mesmo se ele falhar

def test_leitura_arquivo(arquivo_temporario):
    with open(arquivo_temporario) as f:
        conteudo = f.read()
    assert conteudo == "dados de teste"
```

## Mocks: simulando dependências externas

Um **mock** é um objeto "falso" que substitui uma dependência real
durante o teste — útil quando o código depende de algo lento,
não-determinístico, ou externo (uma API, o relógio do sistema, um envio
de e-mail) que você não quer (ou não pode) executar de verdade em um
teste.

```python
# codigo_com_dependencia.py
import requests

def buscar_temperatura(cidade):
    resposta = requests.get(f"https://api-clima.exemplo/{cidade}")
    return resposta.json()["temperatura"]
```

Testar isso chamando a API de verdade seria lento, dependeria de
internet, e o resultado mudaria a cada execução — nada disso é aceitável
em um teste automatizado.

## `unittest.mock`: substituindo o comportamento

```python
from unittest.mock import Mock
from codigo_com_dependencia import buscar_temperatura
import codigo_com_dependencia

def test_buscar_temperatura(monkeypatch):
    resposta_falsa = Mock()
    resposta_falsa.json.return_value = {"temperatura": 25}

    def get_falso(url):
        return resposta_falsa

    monkeypatch.setattr(codigo_com_dependencia.requests, "get", get_falso)

    resultado = buscar_temperatura("Recife")
    assert resultado == 25
```

`monkeypatch` é uma fixture pronta do próprio `pytest` que substitui
temporariamente um atributo/função durante o teste, e **desfaz** a
substituição automaticamente ao final — sem risco de "contaminar" outros
testes.

## Um exemplo mais simples de `monkeypatch`: simulando `input()`

```python
def perguntar_nome():
    return input("Qual o seu nome? ")

def test_perguntar_nome(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt="": "Ana")
    assert perguntar_nome() == "Ana"
```

## Quando usar mock

Use mock/monkeypatch quando o código depende de:
- Chamadas de rede (APIs externas).
- Data/hora atual (`datetime.now()`), quando o teste precisa de um
  resultado previsível.
- Entrada do usuário (`input()`).
- Qualquer recurso lento, caro ou não-determinístico (banco de dados
  real, sistema de arquivos em certos casos).

Não abuse de mocks para código que não tem essas dependências — testar
com os objetos reais (como fizemos com `ContaBancaria`) é mais simples e
mais próximo do comportamento real do sistema.

## Erros comuns

- Usar fixture para dados que **deveriam** ser compartilhados entre
  testes (ex.: um contador que precisa manter estado) — isso quebra o
  isolamento entre testes; cada teste deve começar do zero.
- "Mockar" demais, a ponto de o teste não verificar mais nada real sobre
  o comportamento do código.
- Esquecer que `monkeypatch` desfaz a substituição automaticamente — não
  é necessário (nem possível) "restaurar manualmente" o valor original.

## Boas práticas

- Use fixtures para qualquer setup repetido em 2+ testes.
- Use `yield` em fixtures que precisam de limpeza (teardown) depois do
  teste.
- Reserve mocks para dependências externas de fato (rede, tempo, entrada
  do usuário) — não para simplificar testes de lógica pura.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-06-testes-e-qualidade/aula-02-fixtures-e-mocks/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Introdução a testes com pytest](../aula-01-introducao-a-testes-pytest/aula.md) · ➡️ [Próxima aula: Cobertura e integração contínua](../aula-03-cobertura-e-integracao-continua/aula.md)
