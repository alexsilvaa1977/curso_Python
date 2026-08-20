# Projeto A — API REST de Tarefas

Projeto final que amarra os principais conceitos do curso: POO (via
modelos SQLAlchemy), tratamento de erros (`HTTPException`), persistência
em banco de dados, testes automatizados e uma estrutura de projeto
organizada em camadas — em vez de tudo em um único arquivo, como nos
exemplos das aulas do módulo 8.

## Estrutura do projeto

```
projeto-api-tarefas/
├── app/
│   ├── database.py   # conexão com o banco (SQLAlchemy engine/sessão)
│   ├── models.py      # modelo de dados (tabela "tarefas")
│   ├── schemas.py      # schemas Pydantic de entrada/saída da API
│   ├── crud.py           # funções de acesso a dados (Create/Read/Update/Delete)
│   └── main.py             # rotas da API (FastAPI), conecta tudo
└── tests/
    ├── conftest.py     # fixtures: banco de testes em memória, cliente de teste
    └── test_tarefas.py  # testes das rotas
```

Essa separação em camadas (banco / modelo / schema / regras de acesso a
dados / rotas HTTP) é um padrão comum em APIs Python reais — cada
arquivo tem uma responsabilidade única, o que facilita testar e
evoluir cada parte de forma independente.

## Rotas disponíveis

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/tarefas` | lista todas as tarefas (aceita `?apenas_pendentes=true`) |
| `GET` | `/tarefas/contagem` | retorna `{total, concluidas, pendentes}` |
| `GET` | `/tarefas/{id}` | busca uma tarefa específica |
| `POST` | `/tarefas` | cria uma nova tarefa |
| `PUT` | `/tarefas/{id}` | atualiza campos de uma tarefa (parcial) |
| `DELETE` | `/tarefas/{id}` | remove uma tarefa |

## Como rodar localmente

Na raiz do curso, com o ambiente virtual ativo e as dependências
instaladas (`pip install -r requirements.txt`):

```bash
cd modulo-09-projeto-final/projeto-api-tarefas
uvicorn app.main:app --reload
```

Acesse `http://127.0.0.1:8000/docs` para a documentação interativa
(Swagger UI), onde é possível testar cada rota diretamente do navegador.
Os dados são salvos em um arquivo `tarefas.db` (SQLite), criado
automaticamente na primeira execução — e ignorado pelo git.

## Como rodar os testes

```bash
cd modulo-09-projeto-final/projeto-api-tarefas
pytest -v
```

Os testes usam um banco SQLite **em memória** (configurado em
`tests/conftest.py`), completamente isolado do arquivo `tarefas.db` real
— rodar os testes nunca afeta os dados de desenvolvimento.

## O que este projeto demonstra, módulo a módulo

- **Módulo 4 (POO)**: `Tarefa` (em `models.py`) é uma classe; os schemas
  Pydantic também são classes com validação.
- **Módulo 5 (erros)**: `HTTPException` para comunicar erros de forma
  estruturada (404 quando a tarefa não existe).
- **Módulo 6 (testes)**: suíte de testes com `pytest`, fixtures
  (`conftest.py`) e um banco de dados isolado para testes.
- **Módulo 8 (web/APIs)**: FastAPI, Pydantic, SQLAlchemy — tudo
  integrado em um projeto com mais de um arquivo, em vez de um único
  script de exemplo.

## Ideias para evoluir o projeto (fora do escopo do curso)

- Adicionar autenticação (usuários e login).
- Migrar de SQLite para PostgreSQL (troca de uma linha na URL de
  conexão, graças ao ORM).
- Adicionar paginação em `GET /tarefas` para listas muito grandes.
- Publicar a API em um serviço de hospedagem.

⬅️ [Voltar ao índice do módulo 9](../README.md)
