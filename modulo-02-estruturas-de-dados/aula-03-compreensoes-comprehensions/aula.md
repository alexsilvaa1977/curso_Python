# Aula 3 — Comprehensions

**Objetivos desta aula:**
- Criar listas, dicionários e sets de forma concisa com comprehensions.
- Combinar comprehension com condição (`if`).
- Saber quando **não** usar comprehension (legibilidade acima de tudo).

## List comprehension

Uma forma compacta de criar uma lista a partir de outra sequência,
substituindo um `for` que só serve para preencher uma lista:

```python
# forma tradicional
quadrados = []
for numero in range(10):
    quadrados.append(numero ** 2)

# com list comprehension
quadrados = [numero ** 2 for numero in range(10)]
```

Estrutura geral: `[expressao for item in sequencia]`.

### Com condição (`if`)

```python
pares = [numero for numero in range(20) if numero % 2 == 0]
# equivalente a:
pares = []
for numero in range(20):
    if numero % 2 == 0:
        pares.append(numero)
```

### Com `if`/`else` (expressão condicional dentro da comprehension)

```python
resultado = ["par" if n % 2 == 0 else "ímpar" for n in range(5)]
# ['par', 'ímpar', 'par', 'ímpar', 'par']
```

Note a diferença: o `if` **sem** `else` no final filtra itens; o
`if`/`else` **antes** do `for` transforma cada item.

## Dict comprehension

```python
nomes = ["ana", "bruno", "carla"]
tamanhos = {nome: len(nome) for nome in nomes}
# {'ana': 3, 'bruno': 5, 'carla': 5}
```

```python
precos = {"maçã": 2.5, "banana": 1.8, "uva": 6.0}
precos_com_desconto = {produto: preco * 0.9 for produto, preco in precos.items()}
```

## Set comprehension

```python
palavras = ["python", "java", "python", "go", "java"]
linguagens_unicas = {p.upper() for p in palavras}
# {'PYTHON', 'JAVA', 'GO'}
```

## Comprehension aninhada

Útil para "achatar" listas de listas:

```python
matriz = [[1, 2, 3], [4, 5, 6]]
achatada = [numero for linha in matriz for numero in linha]
# [1, 2, 3, 4, 5, 6]
```

## Quando (não) usar

Comprehensions são ótimas quando a lógica é simples e cabe em uma linha
legível. Se a comprehension começa a ficar difícil de ler (muitos `if`,
lógica aninhada, mais de uma linha), é sinal de que um `for` tradicional
(ou até uma função) vai comunicar melhor a intenção — clareza vale mais
que "economizar linhas".

```python
# Ainda ok
pares_ao_quadrado = [n**2 for n in range(20) if n % 2 == 0]

# Difícil de ler -- prefira um for tradicional aqui
resultado = [x*2 if x % 2 == 0 else x/2 if x % 3 == 0 else x for x in range(30) if x > 5]
```

## Erros comuns

- Esquecer que a ordem é `expressao for item in sequencia`, e não
  `for item in sequencia: expressao` (ordem "invertida" em relação ao
  `for` tradicional costuma confundir no início).
- Criar comprehensions muito complexas, sacrificando legibilidade.
- Usar comprehension só para ter "efeito colateral" (como chamar
  `print()` dentro dela) — isso é um mau uso; comprehension serve para
  **construir uma coleção nova**, não para executar ações.

## Boas práticas

- Use comprehension quando o objetivo é claramente criar uma nova lista/
  dict/set a partir de outra coleção.
- Se precisar de mais de uma condição ou lógica ramificada complexa,
  volte para um `for` tradicional — sua futura leitura de código vai
  agradecer.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Dicionários e sets](../aula-02-dicionarios-e-sets/aula.md) · ➡️ [Próxima aula: Manipulação avançada e desempenho](../aula-04-manipulacao-avancada-e-desempenho/aula.md)
