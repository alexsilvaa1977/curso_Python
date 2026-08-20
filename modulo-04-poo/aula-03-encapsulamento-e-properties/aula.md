# Aula 3 — Encapsulamento e properties

**Objetivos desta aula:**
- Entender a convenção de atributos "protegidos" (`_x`) e "privados" (`__x`).
- Usar `@property` para expor dados com controle/validação.
- Criar setters com `@x.setter` para validar atribuições.

## Encapsulamento: por que esconder dados

Encapsulamento é o princípio de controlar como os dados de um objeto são
acessados e modificados, em vez de deixar qualquer código externo alterar
qualquer atributo livremente e sem validação. Isso evita que o objeto
fique em um estado inválido (ex.: uma idade negativa, um saldo bancário
inconsistente).

## Convenção de nomes: `_protegido` e `__privado`

Python não tem um mecanismo real de "atributo privado" como outras
linguagens — usa **convenção de nomes**:

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular          # público -- acesso livre, sem restrição
        self._saldo = saldo_inicial      # "protegido" (convenção): use com cuidado fora da classe
```

- Um único `_` no início (`_saldo`) é um sinal para outros
  desenvolvedores: "isso é detalhe interno, evite acessar diretamente de
  fora da classe" — mas o Python não impede o acesso.
- Dois `_` no início (`__saldo`) ativa um mecanismo chamado *name
  mangling*: o Python renomeia o atributo internamente
  (`_ContaBancaria__saldo`), tornando o acesso direto de fora bem mais
  difícil (embora ainda não impossível).

```python
class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

conta = ContaBancaria(100)
# print(conta.__saldo)     # ERRO: AttributeError
print(conta._ContaBancaria__saldo)   # funciona, mas ninguém deveria escrever isso
```

Na prática do dia a dia em Python, um único `_` já comunica bem a
intenção "não acesse diretamente"; `__` é usado com mais moderação.

## `@property`: expor um atributo com controle

`@property` permite que um método seja acessado **como se fosse um
atributo** (sem parênteses), permitindo adicionar lógica (cálculo,
validação) de forma transparente para quem usa a classe:

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

conta = ContaBancaria("Ana", 100)
print(conta.saldo)     # 100 -- acessado como atributo, sem "()"
```

## `@x.setter`: controlando a atribuição

Sem um setter, `conta.saldo = -50` daria erro (`property` sem setter é
só leitura). Com `@saldo.setter`, é possível validar o valor antes de
aceitar a atribuição:

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._saldo = novo_valor

conta = ContaBancaria("Ana", 100)
conta.saldo = 200        # usa o setter, passa pela validação
print(conta.saldo)        # 200

conta.saldo = -50         # ERRO: ValueError, a validação bloqueia
```

Do ponto de vista de quem usa a classe, `conta.saldo = 200` parece uma
atribuição simples de atributo — mas por trás, o método `saldo.setter`
está validando o valor. Essa é a vantagem de `property`: a interface
externa continua simples, mesmo com validação por dentro.

## Property somente com getter (somente leitura)

Um caso comum: expor um valor **calculado**, sem permitir atribuição
direta:

```python
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura

r = Retangulo(4, 5)
print(r.area)     # 20 -- calculado, não armazenado
# r.area = 100     # ERRO: AttributeError, não existe setter para "area"
```

## Erros comuns

- Esquecer que `_x` é só uma convenção — nada impede tecnicamente que
  outro código acesse `objeto._x` diretamente; é uma questão de
  comunicação entre desenvolvedores, não de segurança real.
- Criar um `@property` chamado `saldo` mas guardar o dado real também
  como `saldo` (sem `_`) — isso causa recursão infinita, porque o próprio
  getter chamaria a si mesmo. Sempre guarde o dado real com um nome
  diferente (`_saldo`).
- Adicionar `@property` a todo atributo "só para seguir um padrão" — se
  não há validação/cálculo nenhum a fazer, um atributo público comum já
  é suficiente e mais simples.

## Boas práticas

- Comece com atributos públicos simples; adicione `@property` quando
  realmente precisar de validação ou de um valor calculado.
- Prefira `_protegido` (um `_`) na maioria dos casos; reserve `__privado`
  (dois `_`) para casos específicos onde você quer dificultar o acesso
  acidental de fora, especialmente em bibliotecas usadas por outras
  pessoas.
- Sempre valide dentro do setter e levante uma exceção clara
  (`ValueError`, por exemplo) quando o valor não for aceitável.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-04-poo/aula-03-encapsulamento-e-properties/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Herança e polimorfismo](../aula-02-heranca-e-polimorfismo/aula.md) · ➡️ [Próxima aula: Métodos especiais (dunder methods)](../aula-04-metodos-especiais-dunder/aula.md)
