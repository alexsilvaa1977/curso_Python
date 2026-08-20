# Exercícios — Aula 1: Introdução a testes com pytest

1. Crie um módulo `strings_utils.py` com uma função
   `capitalizar_frase(frase)`, e um `test_strings_utils.py` com pelo
   menos dois testes (`assert`).

2. Adicione ao `calculadora.py` uma função `subtrair(a, b)`, e escreva os
   testes correspondentes em `test_calculadora.py`.

3. Escreva um teste que use `pytest.raises` para verificar que uma
   função `validar_idade(idade)` levanta `ValueError` quando a idade é
   negativa.

4. Rode `pytest -v` (modo verboso) sobre os testes que você escreveu e
   leia a saída — identifique quantos testes passaram e quanto tempo
   levou.

5. Escreva um teste que falhe de propósito, rode o `pytest`, e leia
   atentamente a mensagem de erro mostrada — identifique onde o
   `pytest` indica o valor esperado e o valor obtido.

6. **Desafio:** escreva `test_calculadora.py` com pelo menos 6 testes
   cobrindo `somar`, `dividir` (incluindo o caso de erro) e uma nova
   função `multiplicar` que você mesmo vai criar em `calculadora.py`.
   Rode `pytest` e confirme que todos passam.

---
⬅️ [Voltar para a aula](aula.md)
