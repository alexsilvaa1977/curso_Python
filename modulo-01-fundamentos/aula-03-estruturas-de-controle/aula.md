# Aula 3 — Estruturas de controle

**Objetivos desta aula:**
- Controlar o fluxo do programa com `if` / `elif` / `else`.
- Repetir ações com `for` e `while`.
- Usar `break`, `continue` e `range()`.

## Condicionais: `if`, `elif`, `else`

```python
idade = 20

if idade < 12:
    print("criança")
elif idade < 18:
    print("adolescente")
else:
    print("adulto")
```

Regras importantes:
- O bloco depois de `:` precisa estar indentado (4 espaços, por convenção).
- `elif` é opcional e pode se repetir várias vezes.
- `else` é opcional e sempre vem por último.
- Só o **primeiro** bloco cuja condição for verdadeira é executado.

Condicional em uma linha (expressão condicional / "ternário"):

```python
status = "adulto" if idade >= 18 else "menor de idade"
```

## Laço `for`

Usado para percorrer uma sequência (string, lista, `range`, etc.):

```python
for letra in "Python":
    print(letra)
```

```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # início, fim (exclusivo), passo -> 2, 4, 6, 8
    print(i)
```

## Laço `while`

Repete **enquanto** a condição for verdadeira. Use quando não se sabe de
antemão quantas repetições serão necessárias:

```python
tentativas = 0
senha_correta = "python123"
senha_digitada = ""

while senha_digitada != senha_correta and tentativas < 3:
    senha_digitada = input("Digite a senha: ")
    tentativas += 1

if senha_digitada == senha_correta:
    print("Acesso liberado")
else:
    print("Acesso bloqueado")
```

**Cuidado com loop infinito**: se a condição do `while` nunca se tornar
falsa, o programa nunca termina. Sempre garanta que algo dentro do loop
muda o estado testado na condição (como `tentativas += 1` acima).

## `break` e `continue`

- `break` interrompe o laço imediatamente.
- `continue` pula para a próxima iteração, sem executar o resto do bloco.

```python
for numero in range(10):
    if numero == 5:
        break          # para o loop quando chega em 5
    print(numero)
```

```python
for numero in range(10):
    if numero % 2 == 0:
        continue       # pula os números pares
    print(numero)      # só imprime os ímpares
```

## Erros comuns

- Esquecer o `:` no final da linha de `if`/`for`/`while`.
- Indentação inconsistente (misturar 2 e 4 espaços, ou espaços com tabs).
- Loop `while` que nunca termina por esquecer de atualizar a variável de
  controle.
- Usar `elif` depois de um `else` (o `else` deve ser sempre o último bloco).

## Boas práticas

- Prefira `for` quando souber quantas vezes (ou sobre qual coleção) você
  vai iterar; use `while` quando a condição de parada depende de algo que
  só se sabe em tempo de execução.
- Evite `break`/`continue` em excesso — muitos deles no mesmo laço tornam o
  código difícil de seguir. Se estiver difícil de ler, considere extrair
  parte da lógica para uma função (aula 3.1 do módulo 3).

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-01-fundamentos/aula-03-estruturas-de-controle/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Variáveis, tipos e operadores](../aula-02-variaveis-tipos-e-operadores/aula.md) · ➡️ [Próxima aula: Strings e formatação](../aula-04-strings-e-formatacao/aula.md)
