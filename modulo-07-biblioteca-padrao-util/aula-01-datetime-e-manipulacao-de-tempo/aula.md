# Aula 1 — datetime e manipulação de tempo

**Objetivos desta aula:**
- Trabalhar com datas (`date`) e datas com hora (`datetime`).
- Calcular diferenças de tempo com `timedelta`.
- Formatar e converter datas com `strftime`/`strptime`.

## `date`: representando uma data

```python
from datetime import date

hoje = date.today()
print(hoje)             # 2026-08-20 (formato ISO: ano-mês-dia)
print(hoje.year, hoje.month, hoje.day)

aniversario = date(1995, 3, 15)
print(aniversario)
```

## `datetime`: data com hora

```python
from datetime import datetime

agora = datetime.now()
print(agora)                 # 2026-08-20 14:35:02.123456
print(agora.hour, agora.minute, agora.second)

momento_especifico = datetime(2024, 12, 31, 23, 59, 0)
print(momento_especifico)
```

## `timedelta`: diferenças de tempo

`timedelta` representa uma **duração** (dias, horas, minutos...) — usado
tanto para calcular a diferença entre duas datas quanto para "somar" ou
"subtrair" tempo de uma data:

```python
from datetime import date, timedelta

hoje = date.today()
em_10_dias = hoje + timedelta(days=10)
ha_30_dias = hoje - timedelta(days=30)

print(em_10_dias)
print(ha_30_dias)
```

```python
data_nascimento = date(1995, 3, 15)
hoje = date.today()

diferenca = hoje - data_nascimento    # subtrair duas datas dá um timedelta
print(diferenca.days, "dias de vida")
print(diferenca.days // 365, "anos aproximadamente")
```

## Comparando datas

Datas podem ser comparadas diretamente com os operadores que você já
conhece (módulo 1):

```python
data_entrega = date(2026, 12, 25)
hoje = date.today()

if data_entrega > hoje:
    print("Ainda não chegou a data de entrega")
elif data_entrega == hoje:
    print("É hoje!")
else:
    print("A data já passou")
```

## Formatando datas com `strftime`

`strftime` ("string format time") converte um objeto `date`/`datetime`
em uma **string** formatada como você quiser:

```python
agora = datetime.now()

print(agora.strftime("%d/%m/%Y"))         # '20/08/2026'
print(agora.strftime("%Y-%m-%d %H:%M"))    # '2026-08-20 14:35'
print(agora.strftime("%A, %d de %B"))       # nome do dia da semana e do mês (em inglês, por padrão)
```

Principais códigos de formatação:

| Código | Significado |
|---|---|
| `%d` | dia (01-31) |
| `%m` | mês (01-12) |
| `%Y` | ano com 4 dígitos |
| `%H` | hora (00-23) |
| `%M` | minuto |
| `%S` | segundo |
| `%A` | nome do dia da semana |
| `%B` | nome do mês |

## Convertendo texto em data com `strptime`

`strptime` ("string parse time") faz o caminho inverso: transforma uma
**string** em um objeto `datetime`, desde que você informe o formato
exato em que o texto está:

```python
texto = "15/03/1995"
data_convertida = datetime.strptime(texto, "%d/%m/%Y")
print(data_convertida)              # 1995-03-15 00:00:00
print(data_convertida.date())        # 1995-03-15 (só a parte da data)
```

Se o formato informado não corresponder ao texto, `strptime` levanta
`ValueError` (relembrando exceções, módulo 5):

```python
try:
    datetime.strptime("15-03-1995", "%d/%m/%Y")   # formato errado de propósito
except ValueError as erro:
    print("Erro esperado:", erro)
```

## Erros comuns

- Confundir `strftime` (data → texto) com `strptime` (texto → data) —
  um jeito de lembrar: **f**ormat = data para texto **f**ormatado;
  **p**arse = texto **p**arseado para data.
- Comparar `date` com `datetime` diretamente — são tipos diferentes;
  para comparar, use `.date()` em um `datetime` para extrair só a parte
  da data.
- Assumir que `%m` é o mês em texto (é numérico); para nome do mês, use
  `%B`.
- Fazer contas de "anos" dividindo dias por 365 sem considerar anos
  bissextos — é uma aproximação aceitável para a maioria dos casos, mas
  não é exata.

## Boas práticas

- Prefira o formato ISO (`%Y-%m-%d`) para armazenar/trocar datas entre
  sistemas — é não-ambíguo e ordenável como texto.
- Use `timedelta` para qualquer cálculo de "daqui a X dias" ou "diferença
  entre duas datas", em vez de fazer aritmética manual com dias do mês.
- Sempre trate `ValueError` ao converter texto do usuário para data com
  `strptime`.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-07-biblioteca-padrao-util/aula-01-datetime-e-manipulacao-de-tempo/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Voltar ao índice do módulo](../README.md) · ➡️ [Próxima aula: collections, itertools e functools](../aula-02-collections-itertools-e-functools/aula.md)
