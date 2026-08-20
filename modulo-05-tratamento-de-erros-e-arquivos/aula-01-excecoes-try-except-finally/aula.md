# Aula 1 — Exceções: try/except/finally

**Objetivos desta aula:**
- Entender o que é uma exceção e por que ela interrompe o programa.
- Tratar erros com `try`/`except`, capturando exceções específicas.
- Usar `else` e `finally` corretamente.
- Levantar exceções próprias com `raise`.

## O que é uma exceção

Uma exceção é um sinal de que algo deu errado durante a execução — um
tipo de dado inesperado, um arquivo que não existe, uma divisão por
zero. Sem tratamento, uma exceção **interrompe o programa** e mostra um
*traceback*:

```python
idade = int("abc")   # ValueError: invalid literal for int() with base 10: 'abc'
```

Você já viu vários erros desse tipo nas aulas anteriores
(`TypeError`, `KeyError`, `IndexError`, `ValueError`). Cada um é uma
**classe de exceção** diferente, para um tipo diferente de problema.

## `try`/`except`: capturando o erro

```python
try:
    idade = int(input("Digite sua idade: "))
    print(f"Você tem {idade} anos.")
except ValueError:
    print("Isso não é um número válido.")
```

O que acontece:
1. O código dentro de `try` roda normalmente.
2. Se uma exceção do tipo `ValueError` acontecer, o programa **não
   quebra** — em vez disso, pula direto para o bloco `except`.
3. Se não houver exceção, o bloco `except` é ignorado.

## Capturando exceções específicas (não genéricas)

É possível capturar mais de um tipo de exceção, e também acessar a
mensagem de erro:

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
    print(resultado)
except ValueError:
    print("Isso não é um número.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

```python
try:
    numero = int("abc")
except ValueError as erro:
    print("Erro capturado:", erro)   # a mensagem original do Python
```

**Evite `except:` genérico** (sem especificar o tipo) — ele captura
**qualquer** erro, inclusive erros de programação que você provavelmente
queria ver (como um `NameError` por digitar errado o nome de uma
variável), escondendo bugs em vez de tratá-los:

```python
# Evite isso:
try:
    fazer_algo()
except:                 # captura literalmente tudo, inclusive erros que você não previu
    print("Deu erro")

# Prefira ser específico:
try:
    fazer_algo()
except ValueError:
    print("Entrada inválida")
```

Se realmente precisar capturar qualquer exceção (ex.: em um log de
erros de última instância), use `except Exception as erro:` — ainda
específico o suficiente para não esconder erros muito graves do
interpretador (como `KeyboardInterrupt`).

## `else`: código que só roda se **não** houve erro

```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Entrada inválida.")
else:
    print(f"Você digitou {numero}, que ao quadrado é {numero ** 2}.")
```

O bloco `else` só executa se o `try` **não** levantou nenhuma exceção —
útil para separar "o código que pode falhar" do "código que depende do
sucesso do anterior".

## `finally`: código que sempre roda

```python
try:
    arquivo = open("dados.txt")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    print("Tentativa de leitura finalizada.")   # roda com ou sem erro
```

`finally` é usado para "limpeza" que precisa acontecer independente do
resultado (fechar um arquivo, liberar uma conexão) — embora, para
arquivos especificamente, o bloco `with` (aula 3) já cuide disso de
forma mais simples.

## `raise`: levantando uma exceção manualmente

Além de capturar exceções, você pode **provocar** uma, quando seu
próprio código detecta uma situação inválida:

```python
def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor

try:
    sacar(100, 500)
except ValueError as erro:
    print("Operação negada:", erro)
```

## Erros comuns

- Usar `except:` sem especificar o tipo, escondendo bugs reais.
- Capturar a exceção só para "silenciar" o erro (`except: pass`), sem
  nenhum tratamento real — o programa continua rodando em um estado
  possivelmente inválido, sem avisar ninguém.
- Colocar código demais dentro do `try` — quanto mais linhas, mais difícil
  saber exatamente qual delas pode ter causado a exceção capturada.

## Boas práticas

- Capture sempre o tipo de exceção mais específico possível.
- Mantenha o bloco `try` pequeno — só o código que realmente pode
  falhar.
- Trate o erro de verdade (mensagem clara, valor padrão, nova tentativa)
  em vez de só "engolir" a exceção.
- Use `raise` para comunicar problemas de forma explícita em vez de
  retornar valores mágicos como `-1` ou `None` para indicar erro.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-05-tratamento-de-erros-e-arquivos/aula-01-excecoes-try-except-finally/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Voltar ao índice do módulo](../README.md) · ➡️ [Próxima aula: Exceções customizadas](../aula-02-excecoes-customizadas/aula.md)
