# Aula 4 — Tipagem estática: typing e mypy

**Objetivos desta aula:**
- Adicionar *type hints* (dicas de tipo) a variáveis e funções.
- Usar o módulo `typing` para tipos mais expressivos.
- Rodar `mypy` e interpretar os erros que ele encontra.

## O que são type hints

Python é dinamicamente tipado (módulo 1) — mas desde a versão 3.5, é
possível **anotar** o tipo esperado de parâmetros, retornos e variáveis,
sem que isso mude o comportamento do programa em tempo de execução. São
apenas "dicas" — o Python continua rodando normalmente mesmo se elas
estiverem erradas:

```python
def somar(a: int, b: int) -> int:
    return a + b

nome: str = "Ana"
idade: int = 28
```

A sintaxe `parametro: tipo` anota o parâmetro; `-> tipo` (depois dos
parênteses) anota o valor de retorno.

## Por que usar type hints

- **Documentação viva**: fica claro, só de olhar a assinatura da função,
  o que ela espera e o que devolve — sem precisar ler a implementação.
- **Ajuda do editor**: editores como VS Code usam type hints para
  autocompletar e avisar sobre erros antes mesmo de rodar o código.
- **Checagem estática**: ferramentas como `mypy` (veremos a seguir)
  detectam inconsistências de tipo **sem executar o programa**.

## Tipos compostos com o módulo `typing` (e sintaxe moderna)

Para tipos mais elaborados (listas, dicionários, valores opcionais):

```python
from typing import Optional

def buscar_usuario(id_usuario: int) -> Optional[str]:
    """Retorna o nome do usuário, ou None se não encontrado."""
    usuarios = {1: "Ana", 2: "Bruno"}
    return usuarios.get(id_usuario)
```

`Optional[str]` significa "um `str`, ou `None`" — muito comum em funções
que podem não encontrar o que buscam.

Desde o Python 3.9+, é possível usar os próprios tipos genéricos
embutidos (`list`, `dict`) em vez de importar de `typing`:

```python
def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)

def contar_palavras(texto: str) -> dict[str, int]:
    contagem: dict[str, int] = {}
    for palavra in texto.split():
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem
```

Em versões mais antigas (Python 3.8 ou anterior), seria necessário
`from typing import List, Dict` e escrever `List[float]`, `Dict[str,
int]` — hoje, prefira a sintaxe moderna com letra minúscula
(`list[float]`) quando o projeto usa Python 3.9+.

## `Union` (ou o `|` moderno): mais de um tipo possível

```python
def processar_id(id_usuario: int | str) -> str:
    return str(id_usuario)
```

`int | str` significa "um `int` **ou** um `str`" (sintaxe do Python
3.10+; em versões anteriores, `Union[int, str]` do módulo `typing`).

## `mypy`: checando os tipos sem executar o programa

`mypy` lê seu código (com as anotações de tipo) e aponta
inconsistências, sem rodar nada:

```python
# arquivo: exemplo.py
def somar(a: int, b: int) -> int:
    return a + b

resultado = somar(2, "3")   # passando string onde int era esperado
```

```bash
mypy exemplo.py
```

Saída:
```
exemplo.py:4: error: Argument 2 to "somar" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

Note que esse erro é encontrado **sem executar** `exemplo.py` — em
tempo de execução puro, `somar(2, "3")` até daria um erro (`TypeError`
ao tentar `2 + "3"`), mas só quando essa linha específica fosse
executada. `mypy` encontra o problema estaticamente, só de ler o código.

## Corrigindo o erro

```python
def somar(a: int, b: int) -> int:
    return a + b

resultado = somar(2, 3)   # agora os tipos batem
```

```bash
mypy exemplo.py
```
```
Success: no issues found in 1 source file
```

## Type hints são opcionais e graduais

Você não precisa (e normalmente não deve) anotar **tudo** de uma vez em
um projeto existente. É perfeitamente válido ter um arquivo totalmente
tipado e outro sem nenhuma anotação — `mypy` simplesmente não verifica o
que não está anotado. Muitos projetos adotam tipagem gradualmente,
começando pelas partes mais críticas.

## Erros comuns

- Achar que type hints **impedem** o programa de rodar com tipo errado
  — eles não afetam a execução; só `mypy` (ou o editor) os utiliza para
  avisos.
- Anotar tipos genéricos demais (`Any` para tudo) — isso derrota o
  propósito da tipagem estática, já que `mypy` não consegue verificar
  nada de útil contra `Any`.
- Misturar a sintaxe antiga (`List[int]` de `typing`) com a moderna
  (`list[int]`) sem necessidade — em projetos Python 3.9+, prefira a
  moderna por padrão.

## Boas práticas

- Anote pelo menos os parâmetros e o retorno de funções públicas
  (usadas por outras partes do código ou por outras pessoas).
- Use `Optional[X]` (ou `X | None`) sempre que uma função puder
  legitimamente retornar `None`.
- Rode `mypy` como parte da rotina de qualidade do projeto (junto com
  `pytest`, `black`, `flake8`), especialmente antes de integrar código
  novo.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Cobertura e integração contínua](../aula-03-cobertura-e-integracao-continua/aula.md) · ➡️ [Próximo módulo: Biblioteca padrão útil](../../modulo-07-biblioteca-padrao-util/README.md)
