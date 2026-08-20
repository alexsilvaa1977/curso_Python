# Exercícios — Aula 4: Tipagem estática: typing e mypy

1. Adicione type hints completos (parâmetros e retorno) a uma função
   `calcular_area_retangulo(largura, altura)` que você escreveu em
   aulas anteriores.

2. Escreva uma função `buscar_produto(codigo: int, catalogo: dict[int, str]) -> Optional[str]`
   e teste-a com um código que existe e outro que não existe no
   catálogo.

3. Escreva um arquivo com um erro de tipo intencional (ex.: passar um
   `str` onde uma função espera `int`), rode `mypy` sobre ele, e leia a
   mensagem de erro completa.

4. Corrija o erro do exercício 3 e confirme com `mypy` que não há mais
   problemas.

5. Escreva uma função `processar_id(id_usuario: int | str) -> str` que
   aceita tanto `int` quanto `str`, e teste-a com os dois tipos de
   entrada.

6. **Desafio:** pegue um dos scripts de exercício que você escreveu no
   módulo 3 ou 4 (com pelo menos 2-3 funções) e adicione type hints
   completos a todas as funções. Rode `mypy` sobre o arquivo e corrija
   todos os erros até obter "Success: no issues found".

---
⬅️ [Voltar para a aula](aula.md) · ⬅️ [Voltar ao índice do módulo](../README.md)
