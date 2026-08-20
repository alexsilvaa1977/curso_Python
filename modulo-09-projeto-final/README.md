# Módulo 09 — Projeto final

🚧 **Em construção** — este módulo ainda não tem código implementado.
Este README descreve as duas opções de projeto planejadas; a
implementação de cada uma depende dos módulos 4 a 8 (POO, erros/arquivos,
testes, e — na Opção A — web/APIs), que ainda serão escritos.

O projeto final existe para amarrar, na prática, tudo que foi visto no
curso: POO, tratamento de erros, testes automatizados e boas práticas de
organização de projeto. Duas opções são propostas — você pode fazer uma
ou as duas, em momentos diferentes.

## Opção A — API REST de Tarefas (FastAPI)

Um back-end de lista de tarefas (to-do list) com:
- CRUD completo (criar, listar, atualizar, remover tarefas).
- Validação de dados de entrada com Pydantic.
- Persistência em SQLite via SQLAlchemy.
- Testes automatizados com `pytest` e o `TestClient` do FastAPI.

Amarra: POO (modelos de dados), tratamento de erros (exceções HTTP),
persistência em arquivo/banco, testes, e o conteúdo do módulo 8.

## Opção B — CLI de Controle Financeiro Pessoal

Uma aplicação de linha de comando que:
- Registra receitas e despesas em um arquivo JSON ou CSV.
- Usa uma camada de domínio em POO (classes `Transacao`, `Carteira`, etc.).
- Trata erros de entrada do usuário de forma amigável.
- Tem testes unitários cobrindo a lógica de negócio (sem depender de
  frameworks web).

Mais simples que a Opção A — bom como "checkpoint" antes de encarar APIs
web, ou como alternativa para quem quiser focar em lógica de negócio e
testes sem entrar em desenvolvimento web ainda.

## Como este módulo vai evoluir

Quando os módulos 4 a 8 estiverem com conteúdo completo, a implementação
de cada opção será adicionada em subpastas próprias
(`projeto-api-tarefas/` e `projeto-cli-financas/`), cada uma com seu
próprio `README.md`, código-fonte e testes.

⬅️ [Módulo anterior: Web e APIs](../modulo-08-web-e-apis/README.md) | [Índice do curso](../README.md)
