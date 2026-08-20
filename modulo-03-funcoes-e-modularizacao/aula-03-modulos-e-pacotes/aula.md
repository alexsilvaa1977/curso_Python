# Aula 3 — Módulos e pacotes

**Objetivos desta aula:**
- Importar módulos da biblioteca padrão.
- Criar seus próprios módulos e importá-los.
- Organizar módulos relacionados em um pacote.
- Entender o bloco `if __name__ == "__main__":`.

## O que é um módulo

Um módulo é simplesmente um arquivo `.py`. Qualquer script que você
escreveu já é um módulo — a diferença é que, em vez de executá-lo
diretamente, você pode **importar** o que ele contém em outro arquivo.

```python
# arquivo: matematica.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b
```

```python
# arquivo: main.py, na mesma pasta
import matematica

print(matematica.somar(2, 3))       # 5
print(matematica.subtrair(5, 2))     # 3
```

## Formas de importar

```python
import matematica
matematica.somar(2, 3)

from matematica import somar
somar(2, 3)                          # sem precisar do prefixo "matematica."

from matematica import somar as soma  # renomeando na importação
soma(2, 3)

import matematica as mat              # renomeando o módulo inteiro
mat.somar(2, 3)
```

## Módulos da biblioteca padrão

Python já vem com muitos módulos prontos, sem precisar instalar nada:

```python
import math
print(math.sqrt(16))     # 4.0
print(math.pi)             # 3.14159...

import random
print(random.randint(1, 10))    # número aleatório entre 1 e 10
print(random.choice(["a", "b", "c"]))  # escolhe um item aleatório

import datetime
hoje = datetime.date.today()
print(hoje)
```

## `if __name__ == "__main__":`

Quando um arquivo `.py` é executado diretamente, o Python define uma
variável especial `__name__` como `"__main__"`. Quando o mesmo arquivo é
**importado** por outro módulo, `__name__` recebe o nome do módulo, não
`"__main__"`. Isso permite escrever código que só roda quando o arquivo é
executado diretamente — não quando é importado:

```python
# arquivo: matematica.py
def somar(a, b):
    return a + b

if __name__ == "__main__":
    # este bloco só executa se rodarmos "python matematica.py" diretamente
    print("Testando o módulo:")
    print(somar(2, 3))
```

Se outro arquivo fizer `import matematica`, o bloco dentro do `if` **não**
será executado — só as definições de função ficam disponíveis.

## Pacotes: organizando módulos em pastas

Um pacote é uma pasta com vários módulos relacionados, contendo um
arquivo `__init__.py` (pode estar vazio) marcando a pasta como pacote:

```
meu_projeto/
├── main.py
└── utilidades/
    ├── __init__.py
    ├── matematica.py
    └── texto.py
```

```python
# main.py
from utilidades import matematica
from utilidades.texto import capitalizar

print(matematica.somar(2, 3))
print(capitalizar("python"))
```

Desde o Python 3.3, o `__init__.py` não é estritamente obrigatório para
que uma pasta funcione como pacote, mas é uma boa prática mantê-lo
(mesmo vazio) para deixar a intenção explícita e por compatibilidade com
ferramentas mais antigas.

## Erros comuns

- `ModuleNotFoundError` ao importar um módulo que está em outra pasta,
  fora do caminho de busca do Python — o mais simples é manter os
  módulos relacionados na mesma pasta do script principal, ou estruturar
  como pacote.
- Nomear seu próprio arquivo com o mesmo nome de um módulo da biblioteca
  padrão (ex.: criar um `random.py` seu) — isso "esconde" o módulo
  padrão e gera erros confusos.
- Esquecer o `if __name__ == "__main__":` e ter código de teste/execução
  disparando toda vez que o módulo é importado por outro arquivo.

## Boas práticas

- Um módulo deve agrupar funções/dados relacionados a um mesmo assunto
  (ex.: tudo sobre "validação" em um `validacoes.py`).
- Use `if __name__ == "__main__":` para código de teste/demonstração que
  só deve rodar quando o arquivo é executado diretamente.
- Prefira `import modulo` ou `from modulo import coisa_especifica` a
  `from modulo import *` (que importa tudo e torna difícil saber de onde
  vem cada nome usado no código).

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-03-funcoes-e-modularizacao/aula-03-modulos-e-pacotes/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Escopo, args/kwargs e lambdas](../aula-02-escopo-args-kwargs-e-lambdas/aula.md) · ➡️ [Próxima aula: Ambientes virtuais e gerenciamento de dependências](../aula-04-ambientes-virtuais-e-gerenciamento-de-dependencias/aula.md)
