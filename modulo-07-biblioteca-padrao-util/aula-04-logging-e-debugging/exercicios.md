# Exercícios — Aula 4: logging e debugging

1. Configure `logging.basicConfig(level=logging.DEBUG)` e registre uma
   mensagem em cada nível (`debug`, `info`, `warning`, `error`,
   `critical`).

2. Crie um logger nomeado `"estoque"` com `getLogger`, e escreva uma
   função `remover_do_estoque(produto, quantidade, estoque)` que
   registra `INFO` quando a remoção é bem-sucedida e `WARNING` quando
   não há estoque suficiente.

3. Use um formato customizado (`format=...`) que inclua data/hora e
   nível de log, e compare a saída com o formato padrão.

4. Escreva um `try`/`except` que capture uma exceção qualquer e use
   `logging.exception()` para registrá-la — confirme que a saída inclui
   o traceback completo.

5. Copie o exemplo de `breakpoint()` da aula para um arquivo `.py` de
   verdade, execute-o no terminal (`python3 arquivo.py`), e use os
   comandos `n`, `p variavel` e `c` do `pdb` para inspecionar a
   execução.

6. **Desafio:** configure `logging` para escrever as mensagens em um
   arquivo (`logging.basicConfig(filename="app.log", level=logging.INFO)`)
   em vez do terminal, gere algumas mensagens, e depois leia o arquivo
   `app.log` para confirmar que elas foram salvas corretamente.

---
⬅️ [Voltar para a aula](aula.md) · ⬅️ [Voltar ao índice do módulo](../README.md)
