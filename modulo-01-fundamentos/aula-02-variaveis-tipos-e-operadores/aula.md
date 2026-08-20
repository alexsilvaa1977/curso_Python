# Aula 2 — Variáveis, tipos e operadores

**Objetivos desta aula:**
- Criar e nomear variáveis corretamente.
- Conhecer os tipos básicos: `int`, `float`, `str`, `bool`.
- Converter entre tipos (`int()`, `float()`, `str()`).
- Usar operadores aritméticos, de comparação e lógicos.

## Variáveis

Uma variável é um nome que aponta para um valor guardado na memória. Em
Python, você não declara o tipo — ele é inferido a partir do valor:

```python
idade = 28          # int
altura = 1.75        # float
nome = "Ana"          # str
ativo = True          # bool
```

Regras de nomenclatura:
- Pode conter letras, números e `_`, mas não pode **começar** com número.
- Por convenção (PEP 8), use `snake_case`: `nome_completo`, não `nomeCompleto`.
- Evite nomes de uma letra, exceto em contadores curtos (`i`, `j`) ou
  fórmulas matemáticas.
- Não use palavras reservadas (`class`, `for`, `if`, ...) como nome de
  variável.

Python é **dinamicamente tipado**: a mesma variável pode passar a apontar
para um valor de outro tipo:

```python
x = 10        # x é int
x = "dez"     # agora x é str — permitido, mas evite fazer isso sem necessidade
```

## Tipos básicos

| Tipo | Exemplo | Descrição |
|---|---|---|
| `int` | `10`, `-3`, `0` | número inteiro |
| `float` | `3.14`, `-0.5` | número com ponto decimal |
| `str` | `"Python"`, `'ok'` | texto (aspas simples ou duplas) |
| `bool` | `True`, `False` | valor lógico |

Use `type(valor)` para descobrir o tipo de qualquer coisa.

## Conversão de tipos (casting)

`input()` sempre devolve `str`. Para fazer contas, é preciso converter:

```python
idade_texto = input("Sua idade: ")
idade = int(idade_texto)          # converte str -> int
print(idade + 1)
```

```python
int("42")        # 42
float("3.14")    # 3.14
str(42)          # "42"
int("3.14")      # ERRO: ValueError — "3.14" não é um inteiro válido
int(3.99)        # 3 — trunca, não arredonda
```

## Operadores aritméticos

```python
7 + 3    # 10  soma
7 - 3    # 4   subtração
7 * 3    # 21  multiplicação
7 / 3    # 2.333... divisão (sempre retorna float)
7 // 3   # 2   divisão inteira (descarta o resto)
7 % 3    # 1   resto da divisão (módulo)
7 ** 2   # 49  potência
```

`//` e `%` são muito usados: por exemplo, para saber se um número é par,
`numero % 2 == 0`.

## Operadores de comparação

Retornam sempre um `bool` (`True`/`False`):

```python
5 == 5   # True   igual
5 != 3   # True   diferente
5 > 3    # True
5 < 3    # False
5 >= 5   # True
5 <= 4   # False
```

**Atenção**: `=` é atribuição, `==` é comparação. Confundir os dois é um
dos erros mais comuns de quem começa.

## Operadores lógicos

```python
True and False   # False — precisa das duas condições verdadeiras
True or False    # True  — basta uma ser verdadeira
not True         # False — inverte o valor
```

Combinando com comparações:

```python
idade = 20
tem_carteira = True

pode_dirigir = idade >= 18 and tem_carteira
print(pode_dirigir)   # True
```

## Erros comuns

- Confundir `=` com `==`.
- Tentar somar `str` com `int` diretamente: `"idade: " + 25` dá
  `TypeError`. É preciso converter: `"idade: " + str(25)`.
- Esquecer que `input()` retorna sempre texto, e tentar fazer conta direto
  com o resultado sem converter.
- Achar que `/` faz divisão inteira — em Python 3, `/` **sempre** devolve
  `float`; quem faz divisão inteira é `//`.

## Boas práticas

- Dê nomes descritivos às variáveis (`preco_total`, não `pt` ou `x`).
- Prefira `snake_case` para variáveis e funções (padrão PEP 8, ver aula 5).
- Converta tipos explicitamente — nunca dependa de conversões implícitas
  "torcendo" para que funcione.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-01-fundamentos/aula-02-variaveis-tipos-e-operadores/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Introdução e ambiente](../aula-01-introducao-e-ambiente/aula.md) · ➡️ [Próxima aula: Estruturas de controle](../aula-03-estruturas-de-controle/aula.md)
