# Aula 1 — Listas e tuplas

**Objetivos desta aula:**
- Criar, acessar e modificar listas.
- Usar os principais métodos de lista.
- Entender tuplas e quando usá-las em vez de listas.

## Listas

Uma lista é uma coleção **ordenada** e **mutável** de itens, que podem ser
de tipos diferentes (embora, na prática, costumem ser do mesmo tipo):

```python
frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4, 5]
mista = ["Ana", 28, True]     # válido, mas raramente uma boa ideia
```

Acesso por índice (igual a strings — começa em 0, aceita índice negativo):

```python
frutas[0]     # 'maçã'
frutas[-1]    # 'uva'
frutas[1:]    # ['banana', 'uva']
```

## Modificando listas

```python
frutas = ["maçã", "banana", "uva"]

frutas.append("laranja")       # adiciona no fim -> ['maçã', 'banana', 'uva', 'laranja']
frutas.insert(1, "pera")        # insere na posição 1
frutas.remove("banana")         # remove pelo valor (o primeiro encontrado)
ultimo = frutas.pop()            # remove e retorna o último item
frutas[0] = "maçã verde"         # substitui por posição
frutas.sort()                     # ordena a lista, no lugar (in place)
frutas.reverse()                  # inverte a ordem, no lugar
len(frutas)                        # quantidade de itens
```

`sorted(frutas)` (função) devolve uma **nova** lista ordenada, sem alterar
a original — diferente de `frutas.sort()` (método), que ordena a lista
existente. Essa distinção entre "retorna novo" e "modifica no lugar" é
importante e volta a aparecer em outras estruturas.

## Percorrendo listas

```python
for fruta in frutas:
    print(fruta)

for indice, fruta in enumerate(frutas):
    print(indice, fruta)
```

## Listas dentro de listas

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matriz[1][2])   # 6  -> linha 1, coluna 2
```

## Tuplas

Uma tupla é como uma lista, mas **imutável** — depois de criada, não pode
ser alterada:

```python
ponto = (10, 20)
cores = "vermelho", "verde", "azul"   # parênteses são opcionais aqui

# ponto[0] = 99     # ERRO: TypeError, tuplas não suportam atribuição por índice
```

### Quando usar tupla em vez de lista

- Quando o conjunto de valores **não deve mudar** durante a execução
  (ex.: coordenadas, RGB de uma cor, um registro fixo de dados).
- Como chave de dicionário (listas não podem ser chave, por serem
  mutáveis — tuplas podem).
- Levemente mais eficiente em memória e velocidade do que listas, por ser
  imutável.

### Desempacotamento (unpacking)

```python
ponto = (10, 20)
x, y = ponto
print(x, y)    # 10 20

nome, idade, cidade = "Ana", 28, "Recife"
```

## Erros comuns

- Tentar modificar uma tupla (`tupla[0] = 1`) — gera `TypeError`.
- Confundir `.sort()` (modifica no lugar, retorna `None`) com `sorted()`
  (retorna uma nova lista). Um erro clássico:
  ```python
  frutas = frutas.sort()   # BUG: frutas agora é None!
  ```
- Acessar um índice que não existe (`lista[10]` numa lista de 3 itens) —
  gera `IndexError`.
- Usar `list.remove(valor)` pensando que remove por posição — na
  verdade remove pelo **valor**. Para remover por posição, use `del
  lista[indice]` ou `lista.pop(indice)`.

## Boas práticas

- Use tupla para dados que representam um "registro fixo" e lista para
  coleções que crescem/encolhem/mudam durante a execução.
- Prefira `sorted()` quando quiser manter a lista original intacta.
- Use `enumerate()` em vez de controlar um índice manualmente com um
  contador separado.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Voltar ao índice do módulo](../README.md) · ➡️ [Próxima aula: Dicionários e sets](../aula-02-dicionarios-e-sets/aula.md)
