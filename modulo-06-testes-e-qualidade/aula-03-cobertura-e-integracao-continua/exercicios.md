# Exercícios — Aula 3: Cobertura e integração contínua

1. Rode `pytest --cov=calculadora --cov-report=term-missing` nesta pasta
   e identifique quais linhas não estão cobertas antes de adicionar
   qualquer teste novo.

2. Escreva os testes que faltam para `dividir()` e para `eh_par()` (caso
   par e caso ímpar), e confirme que a cobertura sobe para 100%.

3. Escreva um teste "fraco" (que executa uma função sem verificar o
   resultado) e, em um comentário, explique por que ele não deveria
   contar como prova de que o código funciona.

4. Escreva, em um arquivo `.yml`, um workflow de GitHub Actions simples
   que instale as dependências do curso e rode `pytest` a cada `push`
   (baseado no exemplo da aula).

5. Pesquise e explique, em um comentário, a diferença entre cobertura de
   **linhas** (a que vimos) e cobertura de **branches** (galhos de
   `if`/`else`) — por que a segunda é considerada mais rigorosa.

6. **Desafio:** escolha um dos módulos de exercícios que você já
   resolveu em aulas anteriores (por exemplo, do módulo 3 ou 4), escreva
   testes com `pytest` para as funções que você criou, e rode
   `pytest --cov` até atingir pelo menos 90% de cobertura.

---
⬅️ [Voltar para a aula](aula.md)
