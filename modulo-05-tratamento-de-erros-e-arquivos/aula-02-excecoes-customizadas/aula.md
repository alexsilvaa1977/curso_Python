# Aula 2 — Exceções customizadas

**Objetivos desta aula:**
- Criar suas próprias classes de exceção.
- Organizar uma hierarquia de exceções para um domínio específico.
- Saber quando vale a pena criar uma exceção customizada (e quando não).

## Por que criar exceções próprias

As exceções nativas do Python (`ValueError`, `TypeError`, etc.) são
genéricas. Quando seu programa tem regras de negócio específicas
("saldo insuficiente", "usuário não autorizado", "estoque esgotado"),
criar exceções próprias deixa o código mais expressivo e permite tratar
cada situação de forma diferenciada.

## Criando uma exceção customizada

Basta herdar de `Exception` (relembrando herança, aula 2 do módulo 4):

```python
class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(f"Saldo de {saldo} é menor que {valor}")
    return saldo - valor

try:
    sacar(100, 500)
except SaldoInsuficienteError as erro:
    print("Não foi possível sacar:", erro)
```

Por convenção, nomes de exceção terminam com `Error` (ou, mais
raramente, `Exception`).

## Adicionando dados extras à exceção

Uma exceção customizada pode carregar informações além da mensagem,
usando `__init__`:

```python
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_solicitado):
        self.saldo_atual = saldo_atual
        self.valor_solicitado = valor_solicitado
        mensagem = f"Saldo de {saldo_atual} é insuficiente para sacar {valor_solicitado}"
        super().__init__(mensagem)     # passa a mensagem para a classe Exception

try:
    raise SaldoInsuficienteError(saldo_atual=100, valor_solicitado=500)
except SaldoInsuficienteError as erro:
    print(erro)                     # usa a mensagem formatada
    print(erro.saldo_atual)          # e ainda dá para acessar os dados originais
    print(erro.valor_solicitado)
```

## Hierarquia de exceções customizadas

Em um sistema maior, é comum criar uma exceção "base" para o domínio, e
exceções mais específicas herdando dela — permitindo capturar tanto o
erro específico quanto qualquer erro daquele domínio:

```python
class ErroContaBancaria(Exception):
    """Classe base para todos os erros relacionados a conta bancária."""
    pass

class SaldoInsuficienteError(ErroContaBancaria):
    pass

class ContaBloqueadaError(ErroContaBancaria):
    pass

def sacar(conta_bloqueada, saldo, valor):
    if conta_bloqueada:
        raise ContaBloqueadaError("Conta está bloqueada")
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente")
    return saldo - valor

try:
    sacar(conta_bloqueada=True, saldo=100, valor=50)
except ErroContaBancaria as erro:    # captura QUALQUER erro dessa hierarquia
    print(f"Operação bancária falhou: {erro}")
```

Se, em vez disso, você quiser tratar cada erro de forma diferente, basta
capturar as classes específicas em `except` separados — a hierarquia dá
flexibilidade para os dois casos.

## Quando (não) criar uma exceção customizada

Crie uma exceção própria quando:
- O erro representa uma regra de **negócio** específica do seu domínio
  (não apenas "tipo errado" ou "valor inválido" genérico).
- Você quer que quem chama seu código possa capturar esse erro
  especificamente, sem precisar checar o texto da mensagem.

Não crie uma exceção customizada quando uma exceção nativa já descreve o
problema com precisão — por exemplo, se o erro é literalmente "um
argumento do tipo errado foi passado", `TypeError` já é adequado.

## Erros comuns

- Criar uma exceção customizada para todo e qualquer erro, mesmo quando
  uma exceção nativa já serviria — isso adiciona complexidade sem
  benefício real.
- Esquecer `super().__init__(mensagem)` — a exceção customizada perde a
  mensagem legível ao ser impressa (`print(erro)` mostraria vazio).
- Criar hierarquias de exceção excessivamente profundas para projetos
  pequenos — para a maioria dos casos, uma exceção base + algumas
  específicas já é suficiente.

## Boas práticas

- Nomeie exceções terminando com `Error`, de forma descritiva
  (`SaldoInsuficienteError`, não `Erro1`).
- Sempre chame `super().__init__(mensagem)` para manter a mensagem
  acessível.
- Para sistemas com múltiplos tipos de erro relacionados, crie uma
  exceção base do domínio e derive as específicas dela.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Exceções: try/except/finally](../aula-01-excecoes-try-except-finally/aula.md) · ➡️ [Próxima aula: Manipulação de arquivos texto e CSV](../aula-03-manipulacao-de-arquivos-texto-e-csv/aula.md)
