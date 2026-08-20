# Projeto B — CLI de Controle Financeiro Pessoal

Uma aplicação de linha de comando para registrar receitas e despesas,
sem depender de nenhum framework web — foco em modelar bem o domínio
(POO), tratar erros de entrada e ter uma suíte de testes sólida cobrindo
a lógica de negócio.

## Estrutura do projeto

```
projeto-cli-financas/
├── src/
│   ├── dominio.py        # regras de negócio: Transacao, Carteira, exceções
│   ├── persistencia.py    # salvar/carregar em JSON
│   └── cli.py               # interface de linha de comando (argparse)
└── tests/
    ├── test_dominio.py     # testes da lógica de negócio pura
    ├── test_persistencia.py # testes de salvar/carregar
    └── test_cli.py            # testes ponta a ponta da CLI
```

Note que `dominio.py` não sabe nada sobre arquivos, JSON ou linha de
comando — ele só conhece as regras de negócio (uma transação não pode
ter valor zero, o saldo é a soma das transações, etc.). Essa separação
faz com que a lógica mais importante do programa possa ser testada de
forma isolada e rápida, sem tocar em disco.

## Como usar

Na raiz do curso, com o ambiente virtual ativo:

```bash
cd modulo-09-projeto-final/projeto-cli-financas

# adicionar uma receita (valor positivo)
python3 -m src.cli adicionar "Salário" 3000 --categoria renda

# adicionar uma despesa (valor negativo)
python3 -m src.cli adicionar "Aluguel" -1200 --categoria moradia

# listar todas as transações
python3 -m src.cli listar

# listar só uma categoria
python3 -m src.cli listar --categoria moradia

# ver o saldo (receitas - despesas)
python3 -m src.cli saldo

# remover uma transação pelo id mostrado em "listar"
python3 -m src.cli remover 2
```

Por padrão, os dados são salvos em `financas.json` na pasta atual
(ignorado pelo git). Use `--arquivo caminho.json` para usar outro
arquivo — útil para separar, por exemplo, dados de teste dos dados
reais.

## Como rodar os testes

```bash
cd modulo-09-projeto-final/projeto-cli-financas
pytest -v
```

Os testes de `test_cli.py` e `test_persistencia.py` usam a fixture
`tmp_path` do próprio `pytest` (módulo 6) para criar arquivos
temporários — nenhum teste toca no `financas.json` real.

## O que este projeto demonstra, módulo a módulo

- **Módulo 4 (POO)**: `Transacao` (como `dataclass`) e `Carteira`
  encapsulam os dados e as regras do domínio financeiro.
- **Módulo 5 (erros e arquivos)**: exceções customizadas
  (`ValorInvalidoError`, `TransacaoNaoEncontradaError`) e persistência
  em JSON com `pathlib`.
- **Módulo 6 (testes)**: 19 testes cobrindo domínio, persistência e a
  CLI ponta a ponta, incluindo casos de erro.
- **Módulo 7 (stdlib)**: `argparse` para a interface de linha de
  comando, `pathlib` para os caminhos de arquivo, `date` para as datas
  das transações.

## Ideias para evoluir o projeto (fora do escopo do curso)

- Adicionar orçamento por categoria (alertar quando exceder um limite).
- Gerar um relatório mensal resumido.
- Trocar o JSON por um banco SQLite (usando o que foi visto no módulo 8
  e no Projeto A).

⬅️ [Voltar ao índice do módulo 9](../README.md)
