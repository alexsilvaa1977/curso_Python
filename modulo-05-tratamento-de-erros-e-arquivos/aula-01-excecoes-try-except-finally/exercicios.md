# Exercícios — Aula 1: Exceções: try/except/finally

1. Escreva um `try`/`except` que peça um número ao usuário e trate o
   caso de entrada inválida com uma mensagem clara, sem quebrar o
   programa.

2. Escreva uma função `dividir_seguro(a, b)` que retorna o resultado da
   divisão, ou `None` e uma mensagem de erro se `b` for zero (trate
   `ZeroDivisionError`).

3. Escreva um `try`/`except`/`else`/`finally` completo, peça a idade do
   usuário, e: no `except`, avise sobre entrada inválida; no `else`,
   exiba se a pessoa é maior de idade; no `finally`, exiba
   "Processamento concluído" sempre.

4. Escreva uma função `acessar_lista(lista, indice)` que retorna o item
   na posição pedida, ou uma mensagem de erro amigável se o índice não
   existir (capture `IndexError`).

5. Reescreva o código abaixo trocando o `except:` genérico por um
   `except` específico, e explique (em comentário) qual exceção
   realmente pode acontecer ali:
   ```python
   try:
       preco = float(input("Preço: "))
   except:
       print("Erro")
   ```

6. **Desafio:** escreva uma função `processar_pedido(itens)` que recebe
   uma lista de dicionários `{"nome": ..., "preco": ...}`. Para cada
   item, tente calcular `preco * 1.1` (com imposto); se `preco` não for
   um número (capture o erro apropriado), pule esse item e continue os
   demais, acumulando ao final quantos itens falharam.

---
⬅️ [Voltar para a aula](aula.md)
