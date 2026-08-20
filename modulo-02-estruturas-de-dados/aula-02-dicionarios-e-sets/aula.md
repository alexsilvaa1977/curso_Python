# Aula 2 — Dicionários e sets

**Objetivos desta aula:**
- Criar, acessar e modificar dicionários.
- Percorrer dicionários com `.items()`, `.keys()`, `.values()`.
- Usar sets para remover duplicados e comparar coleções.

## Dicionários

Um dicionário guarda pares **chave → valor**. É a estrutura mais usada
para representar um "registro" (como uma linha de banco de dados, ou um
objeto JSON):

```python
pessoa = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "Recife",
}

print(pessoa["nome"])     # 'Ana'
print(pessoa["idade"])    # 28
```

As chaves devem ser de um tipo **imutável** (string, número ou tupla) —
não pode haver duas chaves iguais no mesmo dicionário.

## Modificando dicionários

```python
pessoa["idade"] = 29           # atualiza um valor existente
pessoa["profissao"] = "dev"     # adiciona uma nova chave
del pessoa["cidade"]             # remove uma chave

"nome" in pessoa                 # True -- testa se a chave existe
pessoa.get("telefone")           # None -- não gera erro se a chave não existir
pessoa.get("telefone", "não informado")  # com valor padrão
```

Usar `pessoa["telefone"]` diretamente quando a chave não existe gera
`KeyError`. Por isso, `.get()` é mais seguro quando a chave pode não
estar presente.

## Percorrendo dicionários

```python
for chave in pessoa:
    print(chave, pessoa[chave])

for chave, valor in pessoa.items():
    print(chave, "->", valor)

for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)
```

## Dicionários aninhados

Muito comuns ao representar dados mais complexos (parecido com JSON):

```python
alunos = {
    "aluno1": {"nome": "Ana", "notas": [8, 9, 7]},
    "aluno2": {"nome": "Bruno", "notas": [6, 7, 5]},
}

print(alunos["aluno1"]["nome"])          # 'Ana'
print(alunos["aluno1"]["notas"][0])       # 8
```

## Sets

Um set é uma coleção **não ordenada** de valores **únicos** (sem
duplicados):

```python
frutas = {"maçã", "banana", "maçã", "uva"}
print(frutas)   # {'maçã', 'banana', 'uva'} -- duplicado removido automaticamente

frutas.add("laranja")
frutas.remove("banana")
"uva" in frutas   # True
```

### Operações de conjunto

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # união: {1, 2, 3, 4, 5, 6}
a & b    # interseção: {3, 4}
a - b    # diferença: {1, 2}       (o que está em a, mas não em b)
a ^ b    # diferença simétrica: {1, 2, 5, 6}  (o que não é comum aos dois)
```

### Removendo duplicados de uma lista com set

```python
numeros = [1, 2, 2, 3, 3, 3, 4]
unicos = list(set(numeros))
print(unicos)   # ordem não é garantida, mas duplicados somem
```

## Erros comuns

- Acessar `dicionario["chave_inexistente"]` sem checar antes — gera
  `KeyError`. Use `.get()` ou `if "chave" in dicionario`.
- Achar que sets mantêm a ordem de inserção — eles **não garantem** ordem
  (diferente de listas e, desde o Python 3.7, dicionários).
- Tentar usar uma lista como chave de dicionário ou item de set — gera
  `TypeError`, porque listas são mutáveis (use tupla nesses casos).

## Boas práticas

- Use dicionário quando os dados têm "nome" (chave) — ex.: dados de uma
  pessoa, configuração, resposta de uma API.
- Use set quando a ordem não importa e você só precisa saber "isso existe
  na coleção?" rapidamente, ou remover duplicados.
- Prefira `.get(chave, valor_padrao)` a checar `if chave in dicionario`
  seguido de acesso — é mais direto e evita checagem duplicada.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Listas e tuplas](../aula-01-listas-e-tuplas/aula.md) · ➡️ [Próxima aula: Comprehensions](../aula-03-compreensoes-comprehensions/aula.md)
