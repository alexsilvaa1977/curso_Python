# Aula 1 — Funções, parâmetros e retorno

**Objetivos desta aula:**
- Definir funções com `def`, parâmetros e retorno.
- Usar valores padrão e parâmetros nomeados.
- Escrever docstrings básicas.

## Por que usar funções

Uma função agrupa um bloco de código que faz **uma coisa bem definida**,
com um nome, para poder ser reutilizado sem copiar e colar o código todo
de novo. Se você já copiou e colou o mesmo trecho de código em dois
lugares do seu script, esse é o sinal de que ele deveria ser uma função.

```python
def saudacao(nome):
    return f"Olá, {nome}!"

mensagem = saudacao("Ana")
print(mensagem)     # 'Olá, Ana!'
print(saudacao("Bruno"))   # 'Olá, Bruno!'
```

Partes de uma função:
- `def` inicia a definição.
- `saudacao` é o nome (siga `snake_case`, como variáveis).
- `(nome)` são os **parâmetros** — os "espaços em branco" que a função
  espera receber.
- `return` devolve um valor para quem chamou a função. Sem `return`, a
  função devolve `None` automaticamente.

## Parâmetros com valor padrão

```python
def saudacao(nome, saudacao_inicial="Olá"):
    return f"{saudacao_inicial}, {nome}!"

print(saudacao("Ana"))                    # 'Olá, Ana!'
print(saudacao("Ana", "Bom dia"))          # 'Bom dia, Ana!'
print(saudacao(nome="Ana", saudacao_inicial="Oi"))  # nomeado, ordem não importa
```

Parâmetros com valor padrão devem vir **depois** dos parâmetros
obrigatórios na definição da função.

## Retornando múltiplos valores

Uma função pode retornar mais de um valor — na prática, Python empacota
tudo em uma tupla:

```python
def calcular_estatisticas(numeros):
    menor = min(numeros)
    maior = max(numeros)
    media = sum(numeros) / len(numeros)
    return menor, maior, media

minimo, maximo, media = calcular_estatisticas([4, 8, 15, 16, 23, 42])
print(minimo, maximo, media)
```

## Funções sem retorno explícito

Uma função sem `return` (ou com `return` sem valor) devolve `None`. É
válida quando a função existe apenas para produzir um efeito (como
imprimir algo), não para calcular um valor:

```python
def exibir_relatorio(nome, nota):
    print(f"{nome}: {nota:.1f}")

resultado = exibir_relatorio("Ana", 8.5)
print(resultado)   # None
```

## Docstrings

Uma docstring é um comentário especial (usando `"""`) logo abaixo do
`def`, que documenta o que a função faz:

```python
def calcular_media(numeros):
    """Retorna a média aritmética de uma lista de números."""
    return sum(numeros) / len(numeros)

print(calcular_media.__doc__)   # imprime a docstring
help(calcular_media)              # também mostra a docstring
```

Escreva docstrings para funções cujo nome e assinatura não deixam
totalmente claro o que ela faz, especialmente se outras pessoas (ou você
mesmo, no futuro) vão reutilizá-la.

## Erros comuns

- Esquecer o `return` e assumir que a função "devolveu" algo — ela
  devolveu `None`, silenciosamente.
- Colocar parâmetro obrigatório depois de um com valor padrão
  (`def f(a=1, b)`) — isso é erro de sintaxe.
- Confundir "imprimir" (`print`) com "retornar" (`return`) — uma função
  que só imprime não permite que quem a chamou use o resultado depois.
  ```python
  def soma_errada(a, b):
      print(a + b)     # imprime, mas não retorna

  resultado = soma_errada(2, 3)   # imprime 5
  print(resultado)                  # None -- resultado não foi capturado!
  ```

## Boas práticas

- Uma função deve fazer **uma coisa** e o nome deve deixar isso óbvio
  (`calcular_media`, não `processar` ou `fazer_coisa`).
- Prefira `return` a `print` dentro de funções de lógica — deixe quem
  chama a função decidir o que fazer com o resultado (imprimir, salvar,
  usar em outro cálculo).
- Escreva a docstring pensando em alguém que nunca viu o código.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Voltar ao índice do módulo](../README.md) · ➡️ [Próxima aula: Escopo, args/kwargs e lambdas](../aula-02-escopo-args-kwargs-e-lambdas/aula.md)
