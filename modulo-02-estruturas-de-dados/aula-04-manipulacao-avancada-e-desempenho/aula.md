# Aula 4 — Manipulação avançada e desempenho

**Objetivos desta aula:**
- Usar `sorted()` com `key` para ordenações customizadas.
- Conhecer funções úteis: `zip()`, `map()`, `filter()`.
- Ter uma primeira noção de desempenho (complexidade) ao escolher listas
  vs. dicionários/sets.

## Ordenação customizada com `key`

`sorted()` aceita um parâmetro `key`: uma função que diz **o que** usar
para comparar os itens.

```python
pessoas = [
    {"nome": "Carla", "idade": 25},
    {"nome": "Ana", "idade": 32},
    {"nome": "Bruno", "idade": 19},
]

por_idade = sorted(pessoas, key=lambda p: p["idade"])
por_nome = sorted(pessoas, key=lambda p: p["nome"])
por_idade_decrescente = sorted(pessoas, key=lambda p: p["idade"], reverse=True)
```

`lambda` é uma função anônima de uma linha só (vamos ver com mais detalhe
na aula 2 do módulo 3) — aqui, `lambda p: p["idade"]` diz "para cada
item `p`, use `p["idade"]` como critério de ordenação".

## `zip()`: combinando sequências

```python
nomes = ["Ana", "Bruno", "Carla"]
idades = [28, 34, 25]

for nome, idade in zip(nomes, idades):
    print(nome, idade)

pessoas = dict(zip(nomes, idades))
# {'Ana': 28, 'Bruno': 34, 'Carla': 25}
```

`zip()` para no menor das sequências, se elas tiverem tamanhos diferentes.

## `map()` e `filter()`

Formas funcionais alternativas às comprehensions — em código moderno,
comprehensions costumam ser preferidas por serem mais legíveis, mas você
vai encontrar `map`/`filter` em código de terceiros:

```python
numeros = [1, 2, 3, 4, 5]

dobrados = list(map(lambda n: n * 2, numeros))
# equivalente a: [n * 2 for n in numeros]

pares = list(filter(lambda n: n % 2 == 0, numeros))
# equivalente a: [n for n in numeros if n % 2 == 0]
```

## Uma primeira noção de desempenho

Nem toda estrutura de dados é igualmente rápida para toda operação. Uma
regra prática, sem precisar saber a teoria de complexidade em detalhe:

- **Verificar se um item existe** (`x in colecao`):
  - Em uma **lista**, o Python pode precisar checar item por item —
    fica mais lento conforme a lista cresce.
  - Em um **set** ou **dicionário** (checando chaves), a verificação é
    praticamente instantânea, independente do tamanho.

```python
import time

lista_grande = list(range(1_000_000))
set_grande = set(lista_grande)

inicio = time.perf_counter()
999_999 in lista_grande
print("busca em lista:", time.perf_counter() - inicio)

inicio = time.perf_counter()
999_999 in set_grande
print("busca em set:", time.perf_counter() - inicio)
```

Na prática: se seu programa vai fazer muitas verificações "esse valor já
existe?" em uma coleção grande, considere usar `set` (ou as chaves de um
`dict`) em vez de lista.

## Erros comuns

- Usar `lista.sort(key=...)` quando queria preservar a lista original —
  lembre-se: `.sort()` modifica no lugar, `sorted()` cria uma nova.
- Escrever `lambda` complexos demais — se a lógica não cabe
  confortavelmente em uma linha, defina uma função nomeada (módulo 3) e
  passe ela como `key`.
- Assumir que listas e sets têm a mesma performance para busca — para
  coleções grandes, a diferença é significativa.

## Boas práticas

- Prefira comprehensions a `map`/`filter` em código novo — geralmente são
  mais legíveis para quem está aprendendo Python.
- Ao escolher a estrutura de dados, pergunte-se: "vou precisar checar
  existência com frequência?" Se sim, considere `set`/`dict` em vez de
  `list`.
- Use `key=` em `sorted()` em vez de reordenar manualmente com lógica
  complexa.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Comprehensions](../aula-03-compreensoes-comprehensions/aula.md) · ➡️ [Próximo módulo: Funções e modularização](../../modulo-03-funcoes-e-modularizacao/README.md)
