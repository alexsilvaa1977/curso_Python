# Exercícios — Aula 3: Módulos e pacotes

1. Crie um arquivo `texto_utils.py` com uma função `capitalizar_frase(frase)`
   que capitaliza a primeira letra de cada palavra. Em outro arquivo
   (ou célula), importe e use essa função.

2. Adicione ao `texto_utils.py` um bloco `if __name__ == "__main__":`
   que testa a função com um exemplo fixo, e confirme que ele só executa
   quando você roda `python3 texto_utils.py` diretamente.

3. Use o módulo `random` da biblioteca padrão para sortear 5 números
   diferentes entre 1 e 60 (dica: `random.sample(range(1, 61), 5)`).

4. Use o módulo `datetime` para calcular quantos dias faltam até o fim do
   ano atual, a partir da data de hoje.

5. Crie uma pasta `utilidades/` com um `__init__.py` vazio e dois módulos
   dentro (`matematica.py` e `texto.py`, com pelo menos uma função cada).
   Em um script fora da pasta, importe funções dos dois módulos.

6. **Desafio:** organize os exercícios anteriores de matemática (soma,
   subtração, etc. de aulas passadas) em um módulo `calculadora.py`
   reutilizável, com pelo menos 4 funções, e escreva um `main.py` que
   importa e usa todas elas.

---
⬅️ [Voltar para a aula](aula.md)
