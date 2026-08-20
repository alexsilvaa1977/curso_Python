# Aula 3 — Cobertura e integração contínua

**Objetivos desta aula:**
- Medir cobertura de testes com `pytest-cov`.
- Interpretar um relatório de cobertura sem se obcecar por 100%.
- Entender o que é integração contínua (CI) e ver um exemplo simples.

## O que é cobertura de testes

Cobertura mede **quanto do seu código** é executado quando os testes
rodam — não se o código está correto, apenas se aquelas linhas foram
"visitadas" durante os testes. É uma métrica útil para encontrar código
completamente não testado, mas não é uma garantia de qualidade por si só.

## Medindo cobertura com `pytest-cov`

```bash
pytest --cov=calculadora
```

Saída (resumida):
```
Name             Stmts   Miss  Cover
------------------------------------
calculadora.py       6      1    83%
------------------------------------
TOTAL                6      1    83%
```

- **Stmts**: número de linhas de código executável no arquivo.
- **Miss**: quantas dessas linhas **não** foram executadas por nenhum
  teste.
- **Cover**: percentual de cobertura (`Stmts - Miss` sobre `Stmts`).

Para ver exatamente **quais** linhas não foram cobertas:

```bash
pytest --cov=calculadora --cov-report=term-missing
```

```
Name             Stmts   Miss  Cover   Missing
-----------------------------------------------
calculadora.py       6      1    83%   12
-----------------------------------------------
```

A coluna `Missing` mostra o número da linha não testada — um ponto de
partida direto para saber onde adicionar mais testes.

## Interpretando cobertura (sem se obcecar por 100%)

Cobertura alta **não significa** que os testes são bons — é possível ter
100% de cobertura com testes que não verificam nada de útil:

```python
def test_ruim_mas_com_cobertura():
    somar(2, 3)     # executa a linha, mas não verifica o resultado!
```

Esse teste "cobre" a função `somar`, mas passaria mesmo se `somar`
estivesse quebrada. Cobertura é uma ferramenta para encontrar código
**sem nenhum teste** — não um substituto para pensar sobre a qualidade
dos testes que você escreve.

Uma meta razoável para a maioria dos projetos é buscar cobertura alta
nas partes críticas do sistema (regras de negócio, cálculos importantes)
e não se preocupar tanto com 100% em código trivial (getters simples,
configuração).

## O que é integração contínua (CI)

Integração Contínua é a prática de rodar automaticamente os testes (e
outras verificações, como lint) **a cada mudança** enviada ao
repositório — geralmente a cada `push` ou `pull request` — em um servidor,
sem depender de alguém lembrar de rodar os testes manualmente antes de
enviar o código.

Vantagens:
- Detecta problemas rapidamente, antes que cheguem à branch principal.
- Garante que todo mundo no time roda os testes da mesma forma, no mesmo
  ambiente.
- Serve como um "selo de qualidade" visível em cada mudança (ex.: o
  ícone verde/vermelho ao lado de um PR no GitHub).

## Um exemplo simples de CI com GitHub Actions

GitHub Actions é o serviço de CI integrado ao GitHub. Um arquivo YAML na
pasta `.github/workflows/` descreve o que rodar:

```yaml
# .github/workflows/testes.yml
name: Testes

on: [push, pull_request]

jobs:
  testes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: pytest --cov
```

O que acontece: a cada `push` ou `pull request`, o GitHub cria uma
máquina temporária, instala as dependências e roda `pytest --cov`. Se
algum teste falhar, o GitHub marca aquele commit/PR com um X vermelho —
visível para todo o time antes mesmo de revisar o código manualmente.

Você não precisa implementar isso agora (é conteúdo avançado de DevOps),
mas é importante entender que o mesmo comando `pytest` que você roda no
seu computador é o que roda automaticamente no CI.

## Erros comuns

- Perseguir 100% de cobertura como meta absoluta, escrevendo testes
  fracos só para "marcar a linha como testada".
- Ignorar completamente a cobertura — não ter nenhuma visibilidade sobre
  quais partes do código nunca são exercitadas por nenhum teste.
- Configurar CI que roda os testes, mas ignora o resultado (não bloqueia
  a integração de código com testes falhando).

## Boas práticas

- Use `--cov-report=term-missing` para saber exatamente onde faltam
  testes, não só o percentual total.
- Priorize cobertura em código com lógica de negócio importante.
- Sempre que possível, configure CI desde o início do projeto — é mais
  fácil manter do que adicionar depois de meses sem essa disciplina.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Fixtures e mocks](../aula-02-fixtures-e-mocks/aula.md) · ➡️ [Próxima aula: Tipagem estática: typing e mypy](../aula-04-tipagem-estatica-typing-e-mypy/aula.md)
