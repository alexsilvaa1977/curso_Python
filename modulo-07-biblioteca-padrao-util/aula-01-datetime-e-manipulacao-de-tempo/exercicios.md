# Exercícios — Aula 1: datetime e manipulação de tempo

1. Peça a data de nascimento do usuário (dia, mês, ano, como números
   separados) e calcule quantos dias de vida a pessoa já teve.

2. Escreva uma função `dias_ate(data_futura)` que retorna quantos dias
   faltam até uma data (retorna negativo se a data já passou).

3. Formate a data e hora atuais no padrão brasileiro completo:
   `"20/08/2026 às 14:35"`.

4. Escreva uma função `converter_data_br_para_iso(texto)` que recebe uma
   data no formato `"dd/mm/aaaa"` e retorna no formato ISO
   (`"aaaa-mm-dd"`), tratando `ValueError` se o texto não estiver no
   formato esperado.

5. Calcule que dia da semana será daqui a 100 dias, a partir de hoje
   (dica: `timedelta(days=100)` e `.strftime("%A")`).

6. **Desafio:** escreva uma função `calcular_idade(data_nascimento)` que
   retorna a idade em anos completos (considerando corretamente se o
   aniversário deste ano já passou ou não — não use a aproximação
   `dias // 365`, calcule comparando mês e dia).

---
⬅️ [Voltar para a aula](aula.md)
