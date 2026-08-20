# Aula 2 — collections, itertools e functools

**Objetivos desta aula:**
- Usar `Counter`, `defaultdict` e `namedtuple` do módulo `collections`.
- Usar `itertools` para combinar e percorrer sequências de formas úteis.
- Usar `functools.reduce` e `functools.lru_cache`.

## `collections.Counter`: contando itens

Você já resolveu "contar palavras" manualmente com um `dict` (módulo 2).
`Counter` faz exatamente isso, de forma mais direta:

```python
from collections import Counter

palavras = "python é legal python é útil python vence".split()
contagem = Counter(palavras)
print(contagem)                       # Counter({'python': 3, 'é': 2, 'legal': 1, ...})
print(contagem["python"])              # 3
print(contagem.most_common(2))          # [('python', 3), ('é', 2)] -- os 2 mais comuns
```

## `collections.defaultdict`: dicionário com valor padrão

Evita o padrão repetitivo de checar se uma chave existe antes de usá-la:

```python
# Sem defaultdict
grupos = {}
pessoas = [("A", "Ana"), ("B", "Bruno"), ("A", "Carla")]
for grupo, nome in pessoas:
    if grupo not in grupos:
        grupos[grupo] = []
    grupos[grupo].append(nome)

# Com defaultdict
from collections import defaultdict

grupos = defaultdict(list)          # toda chave nova começa como lista vazia
for grupo, nome in pessoas:
    grupos[grupo].append(nome)      # não precisa checar se a chave já existe

print(dict(grupos))    # {'A': ['Ana', 'Carla'], 'B': ['Bruno']}
```

`defaultdict(list)` cria uma lista vazia automaticamente para qualquer
chave nova acessada; `defaultdict(int)` criaria `0`, útil para
contadores.

## `collections.namedtuple`: tuplas com nomes de campo

Uma alternativa leve a criar uma classe (módulo 4) só para agrupar
alguns valores relacionados, quando você não precisa de métodos:

```python
from collections import namedtuple

Ponto = namedtuple("Ponto", ["x", "y"])

p1 = Ponto(10, 20)
print(p1.x, p1.y)      # acesso por nome, mais legível que p1[0], p1[1]
print(p1)                # Ponto(x=10, y=20)

x, y = p1               # ainda funciona como tupla normal (desempacotamento)
```

## `itertools`: ferramentas para iteração eficiente

### `itertools.chain`: encadeando sequências

```python
from itertools import chain

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

for numero in chain(lista1, lista2):
    print(numero)     # percorre as duas listas como se fosse uma só, sem criar uma nova lista
```

### `itertools.product`: combinações (produto cartesiano)

```python
from itertools import product

cores = ["P", "M"]
tamanhos = ["G", "M"]

for combinacao in product(cores, tamanhos):
    print(combinacao)
# ('P', 'G'), ('P', 'M'), ('M', 'G'), ('M', 'M')
```

### `itertools.groupby`: agrupando itens consecutivos

```python
from itertools import groupby

numeros = [1, 1, 2, 2, 2, 3, 1, 1]

for chave, grupo in groupby(numeros):
    print(chave, list(grupo))
# 1 [1, 1]
# 2 [2, 2, 2]
# 3 [3]
# 1 [1, 1]
```

Note que `groupby` só agrupa elementos **consecutivos** iguais — para
agrupar todos os `1`s independente de posição, seria preciso ordenar a
lista primeiro.

## `functools.reduce`: acumulando um valor

`reduce` aplica uma função acumuladora a todos os itens de uma sequência,
reduzindo-a a um único valor:

```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]

produto = reduce(lambda acumulado, atual: acumulado * atual, numeros)
print(produto)    # 120 (1*2*3*4*5)

# equivalente, mais legível para este caso específico:
produto = 1
for numero in numeros:
    produto *= numero
```

`reduce` é poderoso, mas frequentemente um `for` explícito (ou
`sum()`/`math.prod()` para os casos comuns) é mais legível — use `reduce`
quando a operação de acumulação for realmente customizada.

## `functools.lru_cache`: cache automático de resultados

Guarda o resultado de chamadas anteriores de uma função, evitando
recalcular para os mesmos argumentos — muito útil para funções
"puras" (mesma entrada, sempre mesma saída) e custosas:

```python
from functools import lru_cache
import time

@lru_cache
def calculo_lento(n):
    time.sleep(1)     # simula um cálculo que demora
    return n ** 2

calculo_lento(5)    # demora ~1 segundo
calculo_lento(5)    # instantâneo -- resultado veio do cache
calculo_lento(10)   # demora ~1 segundo de novo -- argumento novo, não está no cache
```

Um uso classico é acelerar funções recursivas, como o cálculo de
Fibonacci:

```python
@lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))    # rápido com cache; sem @lru_cache, seria muito mais lento
```

## Erros comuns

- Usar `defaultdict` e depois se surpreender que uma chave "aparece" no
  dicionário só por ter sido **consultada** (mesmo sem nunca ter sido
  atribuída) — `defaultdict` cria a entrada no primeiro acesso.
- Esperar que `itertools.groupby` agrupe itens iguais em qualquer
  posição da lista — ele só agrupa **consecutivos**; ordene antes se
  precisar do agrupamento completo.
- Usar `@lru_cache` em funções que dependem de estado externo mutável
  (ex.: hora atual, entrada do usuário) — o cache pode devolver um
  resultado "desatualizado".

## Boas práticas

- Prefira `Counter` a montar contagens manualmente com `dict` — é mais
  direto e tem métodos prontos (`most_common`).
- Use `namedtuple` (ou, em código novo, `dataclass` — veremos algo
  parecido em projetos futuros) quando precisar só agrupar dados, sem
  comportamento associado.
- Reserve `@lru_cache` para funções puras e custosas — não é uma
  solução geral para "deixar o código mais rápido".

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-07-biblioteca-padrao-util/aula-02-collections-itertools-e-functools/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: datetime e manipulação de tempo](../aula-01-datetime-e-manipulacao-de-tempo/aula.md) · ➡️ [Próxima aula: os, pathlib e sistema de arquivos](../aula-03-os-pathlib-e-sistema-de-arquivos/aula.md)
