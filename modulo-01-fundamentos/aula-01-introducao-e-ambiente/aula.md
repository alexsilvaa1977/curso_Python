# Aula 1 — Introdução e ambiente

**Objetivos desta aula:**
- Entender o que é Python e por que ele é usado no mercado.
- Instalar/checar o Python e configurar um ambiente virtual.
- Saber executar código de três formas: script `.py`, REPL interativo e Jupyter Notebook.
- Rodar seu primeiro programa.

## O que é Python

Python é uma linguagem de propósito geral, interpretada e de tipagem
dinâmica. É usada em backend web (Django, Flask, FastAPI), automação,
ciência de dados, scripts de infraestrutura e muito mais. Seu ponto forte é
a legibilidade: o código Python lê-se quase como pseudocódigo.

```python
print("Olá, mundo!")
```

Esse é um programa completo e válido em Python — sem `main`, sem
`;`, sem chaves `{}`. A indentação (espaços no início da linha) é o que
delimita blocos de código, então cuidado: em Python, indentação errada é
erro de sintaxe, não só estilo.

## Verificando a instalação

No terminal:

```bash
python3 --version
```

Se aparecer algo como `Python 3.11.6`, está tudo certo. Este curso assume
**Python 3.10 ou superior**.

## Ambiente virtual (venv)

Um ambiente virtual isola as dependências de um projeto das dependências
globais do sistema — evita que a biblioteca de um projeto quebre outro.

```bash
python3 -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate        # Windows
```

Quando o ambiente está ativo, o prompt do terminal costuma mostrar
`(.venv)` no início. A partir daqui, tudo que você instalar com `pip`
fica isolado dentro dessa pasta `.venv/`.

```bash
pip install -r requirements.txt
```

## Três formas de executar Python

1. **Script `.py`** — você escreve o código em um arquivo e executa:
   ```bash
   python3 meu_script.py
   ```
   É o formato usado em programas "de verdade" (o que vira produto).

2. **REPL (modo interativo)** — digitar `python3` no terminal abre um
   console onde cada linha é executada imediatamente. Ótimo para testar uma
   ideia rápida:
   ```bash
   $ python3
   >>> 2 + 2
   4
   >>> exit()
   ```

3. **Jupyter Notebook** — mistura texto explicativo e células de código
   executável, com o resultado aparecendo abaixo de cada célula. É o formato
   usado nos arquivos `exemplos.ipynb` deste curso.
   ```bash
   jupyter notebook
   ```

## Seu primeiro programa

Crie um arquivo `ola.py` com:

```python
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Bem-vindo ao curso de Python.")
```

Execute com `python3 ola.py`. Isso já usa três conceitos que vamos detalhar
na próxima aula: variável (`nome`), entrada de dados (`input`) e formatação
de string (`f"..."`).

## Erros comuns

- **Confundir `python` com `python3`**: em alguns sistemas, `python` ainda
  aponta para Python 2 (ou não existe). Prefira sempre `python3` e `pip3`
  (ou `pip` já dentro do ambiente virtual ativo).
- **Esquecer de ativar o ambiente virtual** antes de instalar pacotes —
  resultado: o pacote é instalado globalmente e pode gerar conflitos.
- **Misturar tabs e espaços** na indentação — configure seu editor para
  usar 4 espaços por nível (é o padrão da comunidade Python, ver PEP 8 na
  aula 5).

## Boas práticas

- Sempre trabalhe dentro de um ambiente virtual por projeto.
- Nomeie o ambiente virtual `.venv` (convenção amplamente usada, já
  ignorada por padrão no `.gitignore` deste repositório).
- Salve as dependências do projeto em `requirements.txt` assim que
  instalar algo novo (`pip freeze > requirements.txt`).

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Voltar ao índice do módulo](../README.md) · ➡️ [Próxima aula: Variáveis, tipos e operadores](../aula-02-variaveis-tipos-e-operadores/aula.md)
