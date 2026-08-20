# Exercícios — Aula 3: Manipulação de arquivos texto e CSV

1. Escreva um script que crie um arquivo `tarefas.txt` com 3 tarefas (uma
   por linha), depois leia e exiba cada tarefa numerada
   (`1. Tarefa X`).

2. Escreva uma função `adicionar_tarefa(caminho, texto)` que usa o modo
   `"a"` para adicionar uma nova tarefa ao arquivo, sem apagar as
   existentes.

3. Escreva um `try`/`except` que tente ler um arquivo que não existe e
   exiba uma mensagem amigável, sem quebrar o programa.

4. Crie um CSV `alunos.csv` com colunas `nome` e `nota`, usando
   `csv.writer`. Depois leia o arquivo com `csv.DictReader` e exiba a
   média das notas.

5. Dado um CSV de produtos com colunas `nome`, `preco`, `estoque`,
   escreva uma função que lê o arquivo e retorna uma lista apenas com os
   produtos que têm `estoque` menor que 5 (produtos "quase esgotando").

6. **Desafio:** escreva um pequeno "banco de dados" em CSV para
   controle de gastos: cada linha tem `data`, `descricao`, `valor`.
   Escreva uma função `adicionar_gasto(caminho, data, descricao, valor)`
   (usando `DictWriter` em modo `"a"`) e outra
   `calcular_total_gastos(caminho)` que lê o arquivo e retorna a soma de
   todos os valores.

---
⬅️ [Voltar para a aula](aula.md)
