# Curso de Python — do zero a desenvolvedor

Curso completo de Python em português, feito para quem já tem alguma base
(sabe o que é uma variável, já rodou algum script) e quer consolidar os
fundamentos e evoluir para o nível de desenvolvedor backend/geral: estruturas
de dados, orientação a objetos, tratamento de erros, testes, boas práticas de
projeto e uma introdução a APIs web.

📖 **Site do curso:** https://alexsilvaa1977.github.io/curso_Python/ — a
mesma navegação abaixo, só que como um site com busca, modo escuro e os
notebooks renderizados direto no navegador.

## Formato das aulas

Cada aula é uma pasta com três arquivos:

- `aula.md` — teoria explicativa: objetivos, conceitos, exemplos comentados,
  erros comuns e boas práticas. Pode ser lido direto no GitHub.
- `exemplos.ipynb` — notebook Jupyter com os exemplos executáveis, para você
  rodar, modificar e experimentar por conta própria.
- `exercicios.md` — exercícios progressivos para fixar o conteúdo (sem
  gabarito — a ideia é você mesmo testar as soluções).

## Pré-requisitos e preparação do ambiente

1. Tenha o **Python 3.10+** instalado (`python3 --version`).
2. Crie e ative um ambiente virtual na raiz do repositório:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```
3. Instale as dependências do curso:
   ```bash
   pip install -r requirements.txt
   ```
4. Abra o Jupyter para acompanhar os notebooks de cada aula:
   ```bash
   jupyter notebook
   ```

## Módulos

| Módulo | Tema | Status |
|---|---|---|
| [01 — Fundamentos](modulo-01-fundamentos/README.md) | Ambiente, variáveis, controle de fluxo, strings, boas práticas | ✅ completo |
| [02 — Estruturas de dados](modulo-02-estruturas-de-dados/README.md) | Listas, tuplas, dicionários, sets, comprehensions | ✅ completo |
| [03 — Funções e modularização](modulo-03-funcoes-e-modularizacao/README.md) | Funções, escopo, `*args`/`**kwargs`, módulos, ambientes virtuais | ✅ completo |
| [04 — Programação Orientada a Objetos](modulo-04-poo/README.md) | Classes, herança, encapsulamento, métodos dunder | ✅ completo |
| [05 — Tratamento de erros e arquivos](modulo-05-tratamento-de-erros-e-arquivos/README.md) | Exceções, arquivos texto/CSV, JSON | ✅ completo |
| [06 — Testes e qualidade](modulo-06-testes-e-qualidade/README.md) | pytest, fixtures/mocks, cobertura, typing | ✅ completo |
| [07 — Biblioteca padrão útil](modulo-07-biblioteca-padrao-util/README.md) | datetime, collections/itertools, pathlib, logging | ✅ completo |
| [08 — Web e APIs](modulo-08-web-e-apis/README.md) | HTTP/REST, Flask, FastAPI, persistência | ✅ completo |
| [09 — Projeto final](modulo-09-projeto-final/README.md) | Projeto prático que amarra todos os conceitos | ✅ completo |

O curso está completo: os 9 módulos têm conteúdo real (não são apenas
esqueletos), incluindo o projeto final com duas aplicações completas e
testadas — veja o [módulo 09](modulo-09-projeto-final/README.md).

## Como estudar

1. Siga os módulos na ordem — cada um assume o conteúdo dos anteriores.
2. Para cada aula: leia o `aula.md`, execute o `exemplos.ipynb` célula por
   célula testando variações, e só depois tente o `exercicios.md` sem
   consultar a aula.
3. Não tem pressa: entender bem os módulos 1 a 3 é o que torna o resto do
   curso (POO, testes, APIs) muito mais fácil.
4. Ao chegar no módulo 9, leia o código-fonte dos dois projetos, rode os
   testes (`pytest -v` dentro de cada pasta de projeto) e tente os
   exercícios de extensão sugeridos em cada README.

## O site do curso

Todo o conteúdo também está publicado como um site (gerado com
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/)) em
**https://alexsilvaa1977.github.io/curso_Python/**, atualizado
automaticamente a cada mudança na branch `main`. O site oferece:

- Navegação por módulo/aula, busca e modo claro/escuro.
- Os notebooks (`exemplos.ipynb`) renderizados como páginas, sem precisar
  instalar Jupyter para só ler o conteúdo.
- Um botão "abrir no Colab" em cada aula, para rodar os exemplos
  interativamente no navegador (sem instalar nada) — veja o link logo
  abaixo de "Exemplos práticos" em cada `aula.md`.

Para gerar o site localmente (opcional — não é necessário para fazer o
curso):

```bash
pip install -r requirements-docs.txt
mkdocs serve   # site em http://127.0.0.1:8000, com live-reload
```

A estrutura de arquivos usada pelo curso (pastas `modulo-NN-.../`) é a
mesma usada como fonte do site — a pasta `_docs/` (versionada, mas
apenas com links simbólicos para o conteúdo real) e o arquivo
`mkdocs.yml` existem só para configurar essa publicação.
