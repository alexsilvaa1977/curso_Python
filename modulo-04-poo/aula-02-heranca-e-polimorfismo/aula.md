# Aula 2 — Herança e polimorfismo

**Objetivos desta aula:**
- Criar classes que herdam de outra classe.
- Usar `super()` para reaproveitar o comportamento da classe pai.
- Sobrescrever métodos e entender polimorfismo na prática.

## Herança: reaproveitando comportamento

Herança permite criar uma classe nova a partir de uma já existente,
reaproveitando seus atributos e métodos e adicionando/especializando o
que for diferente:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "..."

class Cachorro(Animal):     # Cachorro herda de Animal
    def emitir_som(self):    # sobrescreve o método da classe pai
        return "Woof!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

rex = Cachorro("Rex")
print(rex.nome)             # 'Rex' -- herdado de Animal, sem reescrever __init__
print(rex.emitir_som())      # 'Woof!' -- comportamento próprio de Cachorro
```

`Animal` é chamada de **classe pai** (ou superclasse/classe base);
`Cachorro` e `Gato` são **classes filhas** (ou subclasses).

## `super()`: chamando o comportamento da classe pai

Quando a classe filha precisa de um `__init__` (ou outro método)
diferente, mas ainda quer reaproveitar parte do que a classe pai já faz,
usa-se `super()`:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)    # chama o __init__ de Animal, reaproveitando a lógica
        self.raca = raca          # adiciona o que é específico de Cachorro

rex = Cachorro("Rex", "Labrador")
print(rex.nome, rex.raca)   # 'Rex Labrador'
```

Sem `super().__init__(nome)`, seria preciso repetir `self.nome = nome`
manualmente — funcionaria, mas duplicaria código que já existe na classe
pai.

## Polimorfismo: mesmo método, comportamentos diferentes

Polimorfismo é a capacidade de tratar objetos de classes diferentes de
forma uniforme, desde que compartilhem uma "interface" (os mesmos nomes
de método) — cada um responde de um jeito próprio:

```python
animais = [Cachorro("Rex", "Labrador"), Gato("Mimi")]

for animal in animais:
    print(f"{animal.nome}: {animal.emitir_som()}")
# Rex: Woof!
# Mimi: Miau!
```

O código do `for` **não precisa saber** se está lidando com um
`Cachorro` ou um `Gato` — ele só chama `emitir_som()` e cada objeto
"sabe" como se comportar. Esse é o poder do polimorfismo: código genérico
que funciona com qualquer subclasse.

## Verificando o tipo e a hierarquia

```python
print(isinstance(rex, Cachorro))   # True
print(isinstance(rex, Animal))      # True -- Cachorro também é um Animal
print(isinstance(rex, Gato))         # False

print(type(rex))                     # <class '__main__.Cachorro'>
print(Cachorro.__bases__)             # (<class '__main__.Animal'>,)
```

## Herança múltipla (visão geral)

Python permite que uma classe herde de mais de uma classe pai
simultaneamente. É um recurso avançado e usado com moderação — para o
dia a dia, herança simples (de uma classe só) resolve a grande maioria
dos casos:

```python
class Nadador:
    def nadar(self):
        return "nadando..."

class Voador:
    def voar(self):
        return "voando..."

class Pato(Nadador, Voador):    # herda dos dois
    pass

pato = Pato()
print(pato.nadar(), pato.voar())
```

## Erros comuns

- Esquecer `super().__init__(...)` ao sobrescrever `__init__` em uma
  subclasse — os atributos definidos na classe pai simplesmente não são
  criados.
- Criar hierarquias de herança profundas demais (`A → B → C → D → ...`)
  — dificulta entender de onde vem cada comportamento. Prefira hierarquias
  rasas (poucos níveis).
- Usar herança só porque duas classes "parecem" relacionadas, sem que uma
  seja verdadeiramente um caso especial da outra (isso é assunto da
  aula 5, "composição vs. herança").

## Boas práticas

- Use herança quando a relação for genuinamente "é um" (`Cachorro` é um
  `Animal`), não apenas para reaproveitar código de qualquer jeito.
- Sempre chame `super().__init__(...)` quando a subclasse tiver seu
  próprio `__init__`, a menos que você tenha um motivo explícito para não
  reaproveitar a inicialização da classe pai.
- Aproveite o polimorfismo: escreva código que opera sobre a classe pai
  (ou uma interface comum) sempre que possível, em vez de checar o tipo
  exato do objeto com `if isinstance(...)` repetidamente.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Classes, objetos e atributos](../aula-01-classes-objetos-e-atributos/aula.md) · ➡️ [Próxima aula: Encapsulamento e properties](../aula-03-encapsulamento-e-properties/aula.md)
