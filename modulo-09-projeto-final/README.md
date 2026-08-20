# Módulo 09 — Projeto final

O projeto final existe para amarrar, na prática, tudo que foi visto no
curso: POO, tratamento de erros, testes automatizados e boas práticas de
organização de projeto. Duas opções foram implementadas — você pode
estudar/rodar as duas, ou focar na que mais se conecta com o que você
quer fazer como desenvolvedor (web/API ou lógica de negócio/CLI).

## Opção A — [API REST de Tarefas (FastAPI)](projeto-api-tarefas/README.md)

Um back-end de lista de tarefas (to-do list) com:
- CRUD completo (criar, listar, atualizar, remover tarefas).
- Validação de dados de entrada com Pydantic.
- Persistência em SQLite via SQLAlchemy.
- 12 testes automatizados com `pytest` e o `TestClient` do FastAPI.
- Projeto organizado em camadas (`database.py`, `models.py`,
  `schemas.py`, `crud.py`, `main.py`), em vez de um único arquivo.

Amarra: POO (modelos de dados), tratamento de erros (exceções HTTP),
persistência em banco de dados, testes, e o conteúdo do módulo 8.

## Opção B — [CLI de Controle Financeiro Pessoal](projeto-cli-financas/README.md)

Uma aplicação de linha de comando que:
- Registra receitas e despesas em um arquivo JSON.
- Usa uma camada de domínio em POO (`Transacao`, `Carteira`).
- Trata erros de entrada do usuário com exceções customizadas.
- Tem 19 testes unitários cobrindo domínio, persistência e a CLI ponta a
  ponta — sem depender de frameworks web.

Mais simples que a Opção A — bom como "checkpoint" antes de encarar APIs
web, ou como alternativa para quem quiser focar em lógica de negócio e
testes sem entrar em desenvolvimento web.

## Como escolher por onde começar

- Quer seguir para desenvolvimento web/backend com APIs? Comece pela
  **Opção A**.
- Quer reforçar POO, tratamento de erros e testes antes de ir para web?
  Comece pela **Opção B** — ela é mais rápida de entender de ponta a
  ponta.
- O ideal é ler o código-fonte de ambas, rodar os testes, e depois tentar
  os exercícios de extensão sugeridos no README de cada uma.

⬅️ [Módulo anterior: Web e APIs](../modulo-08-web-e-apis/README.md) | [Índice do curso](../README.md)
