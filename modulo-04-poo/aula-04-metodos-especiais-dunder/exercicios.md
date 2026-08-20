# Exercícios — Aula 4: Métodos especiais (dunder methods)

1. Adicione `__str__` e `__repr__` a uma classe `Livro` (com `titulo` e
   `autor`), retornando algo como `"O Alquimista - Paulo Coelho"`.

2. Adicione `__eq__` a uma classe `Fracao` (com `numerador` e
   `denominador`) que considera duas fracões iguais se representarem o
   mesmo valor (ex.: `1/2` igual a `2/4` — dica: compare
   `a.numerador * b.denominador == b.numerador * a.denominador`).

3. Adicione `__len__` a uma classe `Fila` (com uma lista interna) que
   retorna quantos itens estão na fila.

4. Crie uma classe `Vetor2D` com `x` e `y`, e implemente `__add__` para
   que `Vetor2D(1, 2) + Vetor2D(3, 4)` funcione e retorne
   `Vetor2D(4, 6)`.

5. Explique, em um comentário, a diferença prática entre `__str__` e
   `__repr__` com um exemplo: o que `print([objeto])` mostra, e por quê.

6. **Desafio:** crie uma classe `Cronometro` que representa um tempo em
   segundos, com `__repr__` mostrando no formato `"MM:SS"`, e
   `__lt__` (usado por `<`) que permite comparar dois cronômetros e
   ordenar uma lista deles com `sorted()`.

---
⬅️ [Voltar para a aula](aula.md)
