# Aula 5 — Boas práticas: PEP 8 e git básico

**Objetivos desta aula:**
- Escrever código Python no estilo esperado pela comunidade (PEP 8).
- Usar ferramentas automáticas de formatação e lint (`black`, `flake8`).
- Entender o fluxo básico de versionamento com git: `init`, `add`,
  `commit`, `status`, `log`.

## O que é PEP 8

PEP 8 é o guia de estilo oficial da linguagem Python. Ele existe para que
qualquer código Python "pareça" familiar, independente de quem escreveu.
Principais regras:

- **Indentação**: 4 espaços por nível (nunca tabs).
- **Nomes**: `snake_case` para variáveis e funções, `PascalCase` para
  classes, `UPPER_CASE` para constantes.
  ```python
  MAX_TENTATIVAS = 3          # constante
  nome_completo = "Ana Silva"  # variável
  class ContaBancaria:         # classe
      pass
  ```
- **Linhas**: até 79-88 caracteres (a maioria das ferramentas modernas usa
  88, o padrão do `black`).
- **Espaços**: um espaço depois de vírgula, em volta de operadores
  (`a = 1 + 2`, não `a=1+2`).
- **Imports**: um por linha, no topo do arquivo, agrupados (bibliotecas
  padrão, depois bibliotecas de terceiros, depois módulos do próprio
  projeto).

Você não precisa memorizar o documento inteiro — na prática, ferramentas
automáticas cuidam disso.

## Formatação automática com `black`

`black` reformata seu código para seguir um estilo consistente, sem
discussão:

```bash
pip install black
black meu_script.py       # formata o arquivo
black .                    # formata todos os arquivos do projeto
```

## Lint com `flake8`

Um "linter" aponta problemas de estilo e possíveis erros (variável não
usada, import não usado, linha longa) sem executar o código:

```bash
pip install flake8
flake8 meu_script.py
```

## Por que usar essas ferramentas desde já

Em qualquer time de desenvolvimento, o código passa por revisão de outras
pessoas. Código formatado de forma consistente e sem avisos de lint reduz
atrito na revisão e evita bugs bobos (ex.: variável criada e nunca usada,
sinal de que algo foi esquecido).

## Git: por que versionar código desde a primeira aula

Git registra o histórico de mudanças do seu código. Isso permite voltar a
uma versão anterior, entender o que mudou e quando, e trabalhar em equipe
sem sobrescrever o trabalho de outra pessoa. Comandos essenciais:

```bash
git init                      # inicia um repositório na pasta atual
git status                    # mostra o que mudou desde o último commit
git add arquivo.py             # marca um arquivo para ser incluído no próximo commit
git add .                      # marca todos os arquivos modificados
git commit -m "mensagem"       # cria um "ponto de salvamento" com uma mensagem
git log                        # mostra o histórico de commits
git log --oneline              # histórico resumido, uma linha por commit
```

Fluxo típico de trabalho:

```bash
# 1. Você edita arquivos no seu projeto
# 2. Verifica o que mudou
git status

# 3. Adiciona as mudanças que quer salvar
git add nome_do_arquivo.py

# 4. Cria o commit com uma mensagem clara
git commit -m "Adiciona validação de idade no cadastro"

# 5. Confirma no histórico
git log --oneline
```

Boas mensagens de commit descrevem **o que** mudou e, se relevante,
**por quê** — em poucas palavras, no imperativo ("Adiciona", "Corrige",
"Remove"), não no passado ("Adicionei").

## `.gitignore`

Arquivos que não devem ser versionados (ambientes virtuais, caches,
arquivos temporários) vão listados em um arquivo `.gitignore` na raiz do
projeto. Este próprio curso já tem um (`.gitignore` na raiz do
repositório) — vale a pena abri-lo e ler o que está ignorado e por quê.

## Erros comuns

- Comitar o ambiente virtual (`venv/`, `.venv/`) — deixa o repositório
  enorme e depende do sistema operacional de quem criou. Sempre ignore
  essa pasta.
- Mensagens de commit vagas como `"fix"` ou `"update"` — não ajudam
  ninguém (nem você mesmo, meses depois) a entender o histórico.
- Misturar várias mudanças não relacionadas em um único commit — prefira
  commits pequenos e focados em uma mudança lógica.

## Boas práticas

- Rode `black` antes de cada commit (muitos projetos automatizam isso com
  hooks — assunto para depois).
- Escreva mensagens de commit no imperativo e específicas: "Corrige
  cálculo de média na aula 3", não "ajustes".
- Comece a versionar um projeto desde a primeira linha de código, não só
  quando "já está pronto".

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-01-fundamentos/aula-05-boas-praticas-pep8-e-git-basico/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Strings e formatação](../aula-04-strings-e-formatacao/aula.md) · ➡️ [Próximo módulo: Estruturas de dados](../../modulo-02-estruturas-de-dados/README.md)
