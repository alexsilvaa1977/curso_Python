# Exercícios — Aula 4: Manipulação avançada e desempenho

1. Dada uma lista de dicionários representando filmes (`titulo`, `ano`,
   `nota`), ordene por `nota` (do maior para o menor) usando `sorted()`
   com `key`.

2. Use `zip()` para combinar uma lista de nomes de produtos e uma lista
   de preços em um dicionário `{produto: preco}`.

3. Use `map()` para converter uma lista de strings numéricas
   (`["1", "2", "3"]`) em uma lista de inteiros, e depois reescreva a
   mesma operação com list comprehension.

4. Use `filter()` para obter apenas os nomes com mais de 5 letras de uma
   lista, e depois reescreva com list comprehension.

5. Crie uma lista com 200.000 números e um set com os mesmos números.
   Meça (com `time.perf_counter()`) o tempo de verificar se um número que
   **não existe** está na lista, e o tempo de verificar o mesmo número no
   set. Compare os resultados.

6. **Desafio:** dada uma lista de pedidos (dicionários com `cliente` e
   `valor`), ordene primeiro por `cliente` (ordem alfabética) e, para
   pedidos do mesmo cliente, por `valor` (do maior para o menor) — dica:
   `key` pode retornar uma tupla `(cliente, -valor)`.

---
⬅️ [Voltar para a aula](aula.md) · ⬅️ [Voltar ao índice do módulo](../README.md)
