# Exercícios — Aula 4: Serialização: JSON e pickle

1. Converta o dicionário `{"produto": "Teclado", "preco": 150.0}` para
   uma string JSON com `json.dumps()` e exiba o resultado.

2. Salve uma lista de 3 produtos (dicionários com `nome` e `preco`) em um
   arquivo `produtos.json`, formatado com `indent=2`.

3. Leia o `produtos.json` do exercício 2 e calcule o preço total de
   todos os produtos.

4. Escreva uma função `salvar_configuracao(caminho, config)` e
   `carregar_configuracao(caminho)` que usam JSON para persistir um
   dicionário de configurações simples (ex.: `{"tema": "escuro",
   "idioma": "pt-br"}`).

5. Crie uma classe simples `Produto` (com `nome` e `preco`) e escreva o
   código para: (a) tentar serializá-la direto com `json.dumps` e ver o
   erro; (b) convertê-la para dicionário e serializar com sucesso.

6. **Desafio:** escreva uma função `salvar_objeto_pickle(caminho, objeto)`
   e `carregar_objeto_pickle(caminho)`. Use-as para salvar e recuperar
   uma lista de objetos `Produto` (do exercício 5) preservando o tipo
   original — e explique, em um comentário, por que isso não seria
   possível apenas com JSON sem conversão manual.

---
⬅️ [Voltar para a aula](aula.md) · ⬅️ [Voltar ao índice do módulo](../README.md)
