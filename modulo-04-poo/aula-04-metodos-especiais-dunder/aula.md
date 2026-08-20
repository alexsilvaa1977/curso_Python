# Aula 4 — Métodos especiais (dunder methods)

**Objetivos desta aula:**
- Entender o que são "métodos dunder" (`__algo__`).
- Implementar `__str__` e `__repr__` para representações legíveis.
- Implementar `__eq__` para comparar objetos e `__len__` para dar
  suporte a `len()`.

## O que são métodos dunder

"Dunder" vem de *double underscore* (`__`). São métodos especiais que o
Python chama automaticamente em certas situações — como `__init__`
(já visto), chamado ao criar um objeto. Eles permitem que suas próprias
classes se integrem com funções e operadores nativos do Python
(`print()`, `len()`, `==`, `+`, etc.).

## `__str__`: representação amigável (para humanos)

Sem `__str__`, imprimir um objeto mostra algo pouco útil como
`<__main__.Pessoa object at 0x7f...>`. Definindo `__str__`, você controla
o que aparece:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"

ana = Pessoa("Ana", 28)
print(ana)          # 'Ana (28 anos)' -- print() usa __str__ automaticamente
print(str(ana))      # mesma coisa, chamando str() explicitamente
```

## `__repr__`: representação para depuração (para desenvolvedores)

`__repr__` é usado no console interativo, dentro de listas, e como
"plano B" quando `__str__` não existe. A convenção é que `__repr__`
mostre uma representação que, idealmente, ajudaria a recriar o objeto:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Pessoa(nome={self.nome!r}, idade={self.idade})"

ana = Pessoa("Ana", 28)
print(ana)                  # usa __repr__ se __str__ não existir
print([ana, ana])            # dentro de uma lista, sempre usa __repr__
```

Boa prática: implemente pelo menos `__repr__` em suas classes — é o que
aparece em mensagens de erro e no debugger, ajudando muito a entender o
que está acontecendo.

## `__eq__`: comparando objetos com `==`

Sem `__eq__`, `==` compara se dois objetos são **o mesmo objeto na
memória** (equivalente a `is`), não se têm os mesmos dados:

```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Ponto(1, 2)
p2 = Ponto(1, 2)
print(p1 == p2)   # False -- sem __eq__, compara identidade, não dados
```

```python
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

p1 = Ponto(1, 2)
p2 = Ponto(1, 2)
print(p1 == p2)   # True -- agora compara os dados
```

## `__len__`: dando suporte a `len()`

Permite que `len(objeto)` funcione para instâncias da sua classe,
quando fizer sentido (ex.: uma classe que representa uma coleção):

```python
class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def __len__(self):
        return len(self.itens)

carrinho = Carrinho()
carrinho.adicionar("Teclado")
carrinho.adicionar("Mouse")
print(len(carrinho))   # 2 -- len() chama __len__ automaticamente
```

## Outros dunders comuns (visão geral)

Você não precisa memorizar todos agora, mas é útil saber que existem:
`__add__` (permite usar `+` entre objetos), `__lt__`/`__gt__` (permitem
`<`/`>`, úteis para ordenar objetos com `sorted()`), `__getitem__`
(permite `objeto[indice]`), `__iter__` (permite usar `for item in
objeto`).

## Erros comuns

- Definir `__eq__` mas comparar com um objeto de outro tipo sem checar
  — se `outro` não tiver os atributos esperados, o código quebra com
  `AttributeError` em vez de simplesmente retornar `False`.
- Confundir `__str__` (para exibição) com `__repr__` (para depuração) —
  ambos podem coexistir com propósitos diferentes.
- Esquecer que sobrescrever `__eq__` sem também sobrescrever `__hash__`
  torna o objeto "não hasheável" por padrão em versões mais antigas de
  Python — na prática, se você não precisar usar o objeto como chave de
  dicionário ou item de set, isso raramente é um problema no dia a dia.

## Boas práticas

- Implemente `__repr__` na maioria das suas classes — o retorno de
  investimento é alto (ajuda muito na depuração) e o custo é baixo.
- Implemente `__eq__` quando "igualdade de dados" fizer sentido para sua
  classe (ex.: dois `Ponto(1, 2)` devem ser considerados iguais).
- Só implemente os dunders que sua classe realmente precisa — não é
  necessário (nem recomendado) sobrescrever todos "por completude".

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-04-poo/aula-04-metodos-especiais-dunder/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Encapsulamento e properties](../aula-03-encapsulamento-e-properties/aula.md) · ➡️ [Próxima aula: Composição vs. herança](../aula-05-composicao-vs-heranca/aula.md)
