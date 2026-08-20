# Exercícios — Aula 2: collections, itertools e functools

1. Use `Counter` para encontrar a letra mais comum em uma frase (ignore
   espaços).

2. Use `defaultdict(int)` para contar quantos alunos cada professor tem,
   a partir de uma lista de pares `(professor, aluno)`.

3. Crie um `namedtuple` `Produto` com campos `nome`, `preco` e
   `estoque`, crie 3 instâncias, e use `sorted()` para ordená-las por
   `preco`.

4. Use `itertools.product` para gerar todas as combinações possíveis de
   3 tamanhos de camisa (`P`, `M`, `G`) com 2 cores (`azul`, `branco`).

5. Use `functools.reduce` para encontrar o maior número de uma lista,
   sem usar `max()`.

6. **Desafio:** escreva uma função recursiva `fatorial(n)` decorada com
   `@lru_cache`, e compare (com `time.perf_counter()`) o tempo de chamar
   `fatorial(20)` duas vezes — a segunda chamada deve ser
   perceptivelmente mais rápida.

---
⬅️ [Voltar para a aula](aula.md)
