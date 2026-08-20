# Exercícios — Aula 2: Escopo, args/kwargs e lambdas

1. Escreva uma função `multiplicar_tudo(*numeros)` que retorna o produto
   de todos os números recebidos.

2. Escreva uma função `montar_perfil(**dados)` que recebe qualquer
   quantidade de campos nomeados e retorna uma string formatada, por
   exemplo: `"nome: Ana, idade: 28"`.

3. Explique (em um comentário) por que o código abaixo dá erro, e
   corrija-o sem usar `global`:
   ```python
   def dobrar(numero):
       numero = numero * 2

   x = 5
   dobrar(x)
   print(x)  # a pessoa esperava 10, mas x continua 5 -- por quê?
   ```

4. Reescreva estas funções `def` como `lambda`:
   ```python
   def quadrado(x):
       return x ** 2

   def eh_maior_que_dez(x):
       return x > 10
   ```

5. Use `sorted()` com uma `lambda` para ordenar uma lista de strings pelo
   tamanho (menor para maior).

6. **Desafio:** escreva uma função `criar_multiplicador(fator)` que
   **retorna uma função** (`lambda x: x * fator`) já configurada para
   multiplicar por aquele fator. Use-a assim:
   ```python
   triplicar = criar_multiplicador(3)
   print(triplicar(10))  # 30
   ```

---
⬅️ [Voltar para a aula](aula.md)
