# Aula 1 — Classes, objetos e atributos

**Objetivos desta aula:**
- Entender a diferença entre classe e objeto (instância).
- Criar classes com `__init__`, atributos e métodos.
- Diferenciar atributos de instância e atributos de classe.

## Classe vs. objeto

Uma **classe** é um molde que descreve que dados (atributos) e
comportamentos (métodos) um tipo de objeto vai ter. Um **objeto** (ou
**instância**) é uma "cópia concreta" criada a partir desse molde.

Você já usa classes desde a aula 2 do módulo 1, sem saber: `str`, `int`,
`list` e `dict` são todas classes prontas da linguagem. `"Python"` é uma
instância (objeto) da classe `str`.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

ana = Pessoa("Ana", 28)      # ana é um objeto (instância) da classe Pessoa
bruno = Pessoa("Bruno", 34)   # bruno é outro objeto, independente de ana

print(ana.nome, ana.idade)      # Ana 28
print(bruno.nome, bruno.idade)   # Bruno 34
```

## O método `__init__` e o `self`

`__init__` é o **construtor**: roda automaticamente quando um objeto é
criado, e é onde definimos os atributos iniciais. `self` é uma referência
ao próprio objeto sendo criado/manipulado — é sempre o primeiro parâmetro
de qualquer método de instância, e o Python o passa automaticamente
(você nunca escreve `ana.__init__(ana, "Ana", 28)`, só `Pessoa("Ana", 28)`).

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome      # self.nome é o atributo; nome é o parâmetro recebido
        self.idade = idade
```

## Métodos: comportamento do objeto

Um método é uma função definida dentro de uma classe, que opera sobre os
dados (`self.algo`) daquele objeto específico:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Oi, eu sou {self.nome} e tenho {self.idade} anos."

    def fazer_aniversario(self):
        self.idade += 1

ana = Pessoa("Ana", 28)
print(ana.apresentar())     # 'Oi, eu sou Ana e tenho 28 anos.'
ana.fazer_aniversario()
print(ana.idade)             # 29
```

## Atributos de instância vs. atributos de classe

- **Atributo de instância**: definido dentro de `__init__` com `self.`,
  pertence a cada objeto individualmente (cada `Pessoa` tem seu próprio
  `nome` e `idade`).
- **Atributo de classe**: definido diretamente no corpo da classe (fora
  de qualquer método), é **compartilhado** por todas as instâncias.

```python
class Pessoa:
    especie = "Homo sapiens"    # atributo de classe -- igual para todas as instâncias

    def __init__(self, nome, idade):
        self.nome = nome        # atributo de instância -- específico de cada objeto
        self.idade = idade

ana = Pessoa("Ana", 28)
bruno = Pessoa("Bruno", 34)

print(ana.especie, bruno.especie)   # 'Homo sapiens' 'Homo sapiens' -- mesmo valor
print(Pessoa.especie)                 # também acessível pela própria classe
```

Um uso comum de atributo de classe é contar quantas instâncias já foram
criadas:

```python
class Pessoa:
    total_criadas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_criadas += 1     # modifica o atributo de classe

Pessoa("Ana")
Pessoa("Bruno")
print(Pessoa.total_criadas)   # 2
```

## Erros comuns

- Esquecer o `self` como primeiro parâmetro de um método — resulta em
  `TypeError` dizendo que a função recebeu argumentos demais ou de menos.
- Confundir atributo de classe com atributo de instância: modificar um
  atributo de classe **através de uma instância** (`ana.especie = "x"`)
  cria, na verdade, um **novo atributo de instância** que "esconde" o de
  classe só para aquele objeto — não altera o valor para as outras
  instâncias.
- Esquecer de usar `self.` ao criar um atributo dentro de `__init__`
  (`nome = nome` em vez de `self.nome = nome`) — a variável desaparece
  quando o método termina, e o objeto nunca guarda esse dado.

## Boas práticas

- Nomeie classes em `PascalCase` (`Pessoa`, `ContaBancaria`) e
  instâncias/variáveis em `snake_case` (`ana`, `conta_corrente`).
- Uma classe deve representar um conceito coeso — se está difícil
  resumir "o que essa classe representa" em uma frase, ela provavelmente
  está fazendo coisas demais.
- Use atributos de classe apenas para dados realmente compartilhados por
  todas as instâncias (constantes, contadores); para dados específicos
  de cada objeto, sempre atributo de instância.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Voltar ao índice do módulo](../README.md) · ➡️ [Próxima aula: Herança e polimorfismo](../aula-02-heranca-e-polimorfismo/aula.md)
