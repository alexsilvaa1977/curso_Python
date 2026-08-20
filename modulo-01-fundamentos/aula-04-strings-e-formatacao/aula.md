# Aula 4 — Strings e formatação

**Objetivos desta aula:**
- Manipular texto: indexação, slicing, métodos comuns.
- Formatar strings com f-strings.
- Entender que strings são imutáveis.

## Strings são sequências

Uma string pode ser tratada como uma sequência de caracteres, com índices
começando em `0`:

```python
palavra = "Python"
print(palavra[0])    # 'P'
print(palavra[-1])   # 'n'  (índice negativo conta do fim)
print(len(palavra))  # 6
```

## Slicing (fatiamento)

```python
palavra = "Python"
print(palavra[0:3])    # 'Pyt'   (do índice 0 até o 3, exclusivo)
print(palavra[:3])     # 'Pyt'   (do início até o 3)
print(palavra[3:])     # 'hon'   (do 3 até o fim)
print(palavra[::-1])   # 'nohtyP' (string invertida)
print(palavra[::2])    # 'Pto'   (pula de 2 em 2)
```

## Strings são imutáveis

Não é possível alterar um caractere "no lugar":

```python
palavra = "Python"
# palavra[0] = "J"     # ERRO: TypeError

nova_palavra = "J" + palavra[1:]
print(nova_palavra)    # 'Jython'
```

Qualquer operação que "modifica" uma string, na verdade, cria uma string
**nova**.

## Métodos úteis de string

```python
texto = "  Curso de Python  "

texto.strip()          # 'Curso de Python'      remove espaços das pontas
texto.lower()           # '  curso de python  '  minúsculas
texto.upper()           # '  CURSO DE PYTHON  '  maiúsculas
texto.replace("Python", "Django")  # troca substrings
texto.split()            # ['Curso', 'de', 'Python']  quebra em lista
"-".join(["a", "b", "c"])  # 'a-b-c'   junta lista em string
texto.strip().startswith("Curso")  # True
"python" in texto.lower()          # True — testa se contém substring
```

## Formatação com f-strings

A forma moderna e recomendada de compor strings com valores:

```python
nome = "Ana"
idade = 28

print(f"{nome} tem {idade} anos.")

# expressões dentro das chaves são avaliadas
print(f"No ano que vem, {nome} terá {idade + 1} anos.")

# controle de formatação numérica
preco = 19.9
print(f"Preço: R$ {preco:.2f}")        # duas casas decimais -> R$ 19.90

percentual = 0.256
print(f"{percentual:.1%}")              # formata como porcentagem -> 25.6%
```

Formas mais antigas que você vai encontrar em código legado (bom saber
ler, mas prefira f-strings em código novo):

```python
"{} tem {} anos".format(nome, idade)     # .format()
"%s tem %d anos" % (nome, idade)          # % antigo, estilo C
```

## Erros comuns

- Esquecer o `f` antes das aspas e as chaves `{}` aparecerem literalmente
  no texto em vez do valor.
- Tentar alterar um caractere de uma string diretamente (`texto[0] = "X"`)
  — strings são imutáveis; crie uma nova string.
- Confundir `str.strip()` (remove espaço das pontas) com `str.replace(" ", "")`
  (remove **todos** os espaços).
- Índice fora do intervalo (`texto[100]` numa string de 6 caracteres) —
  gera `IndexError`.

## Boas práticas

- Use f-strings para qualquer composição de texto com variáveis.
- Sempre trate a entrada do usuário com `.strip()` antes de comparar, para
  evitar bugs por espaços acidentais (`"sim "` != `"sim"`).
- Para comparar textos ignorando maiúsculas/minúsculas, normalize com
  `.lower()` dos dois lados: `resposta.lower() == "sim"`.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-01-fundamentos/aula-04-strings-e-formatacao/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Estruturas de controle](../aula-03-estruturas-de-controle/aula.md) · ➡️ [Próxima aula: Boas práticas — PEP 8 e git básico](../aula-05-boas-praticas-pep8-e-git-basico/aula.md)
