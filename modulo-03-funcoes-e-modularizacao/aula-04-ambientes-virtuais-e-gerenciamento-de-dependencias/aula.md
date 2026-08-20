# Aula 4 — Ambientes virtuais e gerenciamento de dependências

**Objetivos desta aula:**
- Entender por que cada projeto deve ter seu próprio ambiente virtual.
- Instalar, listar e "congelar" dependências com `pip`.
- Conhecer `requirements.txt` e uma introdução a `pyproject.toml`.

## Por que isolar dependências por projeto

Imagine dois projetos: o Projeto A precisa da versão 1.0 de uma
biblioteca, e o Projeto B precisa da versão 2.0 da mesma biblioteca. Se
você instalar tudo "globalmente" no sistema, só uma das versões pode
estar instalada por vez — os projetos entram em conflito.

Um **ambiente virtual** cria uma cópia isolada do interpretador Python e
de seus pacotes instalados, por projeto. Já vimos como criar um na aula 1
do módulo 1:

```bash
python3 -m venv .venv
source .venv/bin/activate       # Linux/macOS
# .venv\Scripts\activate         # Windows
```

Com o ambiente ativo, tudo que for instalado com `pip` fica isolado
dentro da pasta `.venv/` daquele projeto.

## Instalando e gerenciando pacotes com `pip`

```bash
pip install requests               # instala a última versão
pip install requests==2.31.0        # instala uma versão específica
pip install "requests>=2.28,<3.0"   # instala dentro de uma faixa de versões
pip list                             # lista pacotes instalados no ambiente ativo
pip show requests                    # detalhes de um pacote instalado
pip uninstall requests                # remove um pacote
```

## `requirements.txt`

É a forma mais comum de declarar as dependências de um projeto Python,
para que qualquer pessoa (ou servidor de produção) possa recriar o mesmo
ambiente:

```bash
pip freeze > requirements.txt    # gera o arquivo com as versões exatas instaladas
pip install -r requirements.txt   # instala tudo que está listado no arquivo
```

Um `requirements.txt` típico:

```
requests==2.31.0
flask==3.0.0
pytest==7.4.3
```

Fixar a versão exata (`==`) garante reprodutibilidade: o mesmo
`requirements.txt` instala exatamente os mesmos pacotes em qualquer
máquina, evitando o clássico "funciona na minha máquina".

## Uma introdução a `pyproject.toml`

`pyproject.toml` é o padrão mais moderno para configurar um projeto
Python — além de dependências, ele também guarda metadados do projeto
(nome, versão) e configuração de ferramentas (`black`, `pytest`, `mypy`).
Este próprio curso já tem um na raiz do repositório:

```toml
[tool.black]
line-length = 88

[tool.pytest.ini_options]
testpaths = ["modulo-09-projeto-final"]
```

Para projetos simples como os deste curso, `requirements.txt` já resolve
bem. `pyproject.toml` se torna mais importante quando o projeto vira um
**pacote instalável** (algo que outras pessoas instalam com
`pip install seu_projeto`) — voltamos a esse ponto no módulo do projeto
final.

## Erros comuns

- Instalar pacotes sem o ambiente virtual ativo — eles vão para o Python
  "global" do sistema, o que pode causar conflitos entre projetos
  diferentes.
- Comitar a pasta `.venv/` no git — ela é grande, específica da máquina, e
  totalmente recriável a partir do `requirements.txt` (por isso está no
  `.gitignore`).
- Esquecer de atualizar o `requirements.txt` depois de instalar um pacote
  novo — na hora que outra pessoa (ou você, em outra máquina) tentar
  rodar o projeto, vai faltar a dependência.

## Boas práticas

- Um ambiente virtual por projeto, sempre.
- Atualize o `requirements.txt` (`pip freeze > requirements.txt`) sempre
  que instalar ou remover uma dependência.
- Nunca versione `.venv/`; sempre versione `requirements.txt`.
- Ao clonar/baixar um projeto de outra pessoa, o primeiro passo é sempre:
  criar o ambiente virtual e rodar `pip install -r requirements.txt`.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Módulos e pacotes](../aula-03-modulos-e-pacotes/aula.md) · ➡️ [Próximo módulo: POO](../../modulo-04-poo/README.md)
