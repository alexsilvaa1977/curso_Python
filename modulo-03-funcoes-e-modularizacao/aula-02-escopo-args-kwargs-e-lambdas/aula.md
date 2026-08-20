# Aula 2 — Escopo, `*args`/`**kwargs` e lambdas

**Objetivos desta aula:**
- Entender escopo local vs. global.
- Criar funções com número variável de argumentos (`*args`, `**kwargs`).
- Escrever e usar funções `lambda`.

## Escopo local vs. global

Uma variável criada **dentro** de uma função só existe dentro dela
(escopo local). Uma variável criada fora de qualquer função (escopo
global) pode ser **lida** de dentro de funções, mas não modificada
diretamente:

```python
contador_global = 0

def incrementar():
    contador_local = 10   # só existe dentro desta função
    print(contador_global)  # OK, ler uma variável global funciona
    return contador_local

incrementar()
print(contador_local)   # ERRO: NameError, contador_local não existe aqui fora
```

Para **modificar** uma variável global dentro de uma função, é preciso a
palavra-chave `global` (só use isso quando realmente necessário — é
considerado uma prática arriscada, porque dificulta rastrear quem alterou
o quê):

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
print(contador)   # 2
```

Prefira sempre retornar o novo valor em vez de usar `global`:

```python
def incrementar(valor_atual):
    return valor_atual + 1

contador = 0
contador = incrementar(contador)
contador = incrementar(contador)
print(contador)   # 2
```

## `*args`: número variável de argumentos posicionais

```python
def somar_tudo(*numeros):
    return sum(numeros)

print(somar_tudo(1, 2))          # 3
print(somar_tudo(1, 2, 3, 4, 5))  # 15
```

Dentro da função, `numeros` é uma tupla com todos os argumentos
passados, independente de quantos forem.

## `**kwargs`: número variável de argumentos nomeados

```python
def exibir_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_dados(nome="Ana", idade=28, cidade="Recife")
```

Dentro da função, `dados` é um dicionário com todos os argumentos
nomeados passados.

## Combinando parâmetros normais, `*args` e `**kwargs`

A ordem na definição da função é sempre: parâmetros normais, depois
`*args`, depois `**kwargs`:

```python
def registrar_pedido(cliente, *itens, **detalhes):
    print("Cliente:", cliente)
    print("Itens:", itens)
    print("Detalhes:", detalhes)

registrar_pedido("Ana", "camisa", "calça", forma_pagamento="cartão", parcelas=3)
```

## Funções `lambda`

Uma `lambda` é uma função anônima, de uma única expressão, sem `def` e
sem nome (a menos que você a atribua a uma variável):

```python
dobro = lambda x: x * 2
print(dobro(5))   # 10

# equivalente a:
def dobro(x):
    return x * 2
```

`lambda` é útil principalmente como argumento "descartável" para outras
funções, como já vimos com `sorted(..., key=lambda item: item["idade"])`:

```python
pessoas = [{"nome": "Ana", "idade": 28}, {"nome": "Bruno", "idade": 19}]
pessoas_ordenadas = sorted(pessoas, key=lambda p: p["idade"])
```

## Erros comuns

- Tentar acessar uma variável local fora da função onde ela foi criada.
- Usar `global` como forma padrão de "compartilhar" dados entre funções
  — em vez disso, passe valores como parâmetro e retorne o resultado.
- Escrever lambdas muito complexas — se precisar de mais de uma linha
  de lógica, use `def` com um nome, não force tudo em uma `lambda`.

## Boas práticas

- Evite `global` — prefira passar e retornar valores explicitamente.
- Use `*args`/`**kwargs` quando o número de argumentos realmente varia
  (ex.: uma função de log que aceita qualquer quantidade de mensagens).
- Reserve `lambda` para expressões curtas e óbvias, geralmente como
  argumento de outra função (`key=`, `sorted`, etc.).

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-03-funcoes-e-modularizacao/aula-02-escopo-args-kwargs-e-lambdas/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Funções, parâmetros e retorno](../aula-01-funcoes-parametros-e-retorno/aula.md) · ➡️ [Próxima aula: Módulos e pacotes](../aula-03-modulos-e-pacotes/aula.md)
