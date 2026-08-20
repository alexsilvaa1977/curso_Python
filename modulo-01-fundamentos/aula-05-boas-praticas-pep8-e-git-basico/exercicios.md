# Exercícios — Aula 5: PEP 8 e git básico

1. Pegue um script que você escreveu em uma aula anterior e reescreva os
   nomes de variáveis que não seguem `snake_case`.

2. Instale `black` e `flake8` (`pip install -r requirements.txt` na raiz
   do curso) e rode `flake8` sobre um dos seus scripts de exercício.
   Corrija os avisos que aparecerem.

3. Crie uma pasta nova fora deste repositório, rode `git init`, crie um
   arquivo `ola.py` com um `print`, e faça seu primeiro commit com uma
   mensagem clara.

4. No mesmo repositório de teste, modifique o arquivo `ola.py`, rode
   `git status` (para ver a mudança pendente) e depois `git diff` (para
   ver exatamente o que mudou linha a linha), e então faça um segundo
   commit.

5. Rode `git log --oneline` e confirme que os dois commits aparecem no
   histórico, do mais recente para o mais antigo.

6. **Desafio:** escreva um `.gitignore` para esse repositório de teste
   cobrindo pelo menos `__pycache__/` e `.venv/`, crie esses arquivos/pastas
   propositalmente e confirme com `git status` que eles não aparecem como
   "untracked".

---
⬅️ [Voltar para a aula](aula.md) · ⬅️ [Voltar ao índice do módulo](../README.md)
