# Exercícios — Aula 3: os, pathlib e sistema de arquivos

1. Crie um `Path` juntando 3 partes (`"projeto"`, `"src"`,
   `"main.py"`) usando o operador `/`, e exiba `.name`, `.parent` e
   `.suffix`.

2. Crie uma estrutura de pastas `relatorios/2024/janeiro` de uma vez só
   com `mkdir(parents=True, exist_ok=True)`.

3. Escreva uma função `contar_arquivos_por_extensao(pasta)` que retorna
   um dicionário `{extensão: quantidade}` para todos os arquivos de uma
   pasta (dica: combine `iterdir()` com `Counter` da aula anterior).

4. Escreva uma função `criar_arquivo_se_nao_existir(caminho, conteudo)`
   que só escreve o arquivo se ele ainda não existir (verifique com
   `.exists()` antes).

5. Use `.rglob("*.py")` para listar (de forma recursiva) todos os
   arquivos `.py` de exemplo criados neste curso, a partir da raiz do
   repositório.

6. **Desafio:** escreva uma função `organizar_por_extensao(pasta_origem)`
   que move (ou copia, se preferir mais seguro) cada arquivo de uma
   pasta para uma subpasta nomeada com sua extensão (ex.: todos os
   `.txt` vão para `pasta_origem/txt/`), criando as subpastas
   conforme necessário.

---
⬅️ [Voltar para a aula](aula.md)
