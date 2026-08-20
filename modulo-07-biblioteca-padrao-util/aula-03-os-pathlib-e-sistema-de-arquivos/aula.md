# Aula 3 — os, pathlib e sistema de arquivos

**Objetivos desta aula:**
- Entender por que `pathlib.Path` é preferível a manipular caminhos como
  string.
- Criar, listar e verificar arquivos/diretórios.
- Juntar caminhos de forma portátil entre sistemas operacionais.

## O problema de manipular caminhos como texto

```python
# Frágil: funciona no Linux/macOS, quebra no Windows (separador diferente)
caminho = "dados" + "/" + "relatorio.txt"
```

Windows usa `\` como separador de caminho; Linux/macOS usam `/`.
Concatenar strings manualmente é uma fonte comum de bugs "só no Windows"
(ou vice-versa).

## `pathlib.Path`: a forma moderna e recomendada

```python
from pathlib import Path

caminho = Path("dados") / "relatorio.txt"
print(caminho)          # 'dados/relatorio.txt' (ou 'dados\relatorio.txt' no Windows)
```

O operador `/` entre objetos `Path` (e strings) junta caminhos de forma
que funciona corretamente em qualquer sistema operacional — o `pathlib`
decide o separador certo internamente.

## Informações sobre um caminho

```python
caminho = Path("dados/relatorio_2024.txt")

print(caminho.name)         # 'relatorio_2024.txt' -- nome do arquivo, com extensão
print(caminho.stem)          # 'relatorio_2024' -- nome sem extensão
print(caminho.suffix)         # '.txt' -- só a extensão
print(caminho.parent)          # 'dados' -- pasta que contém o arquivo
print(caminho.parts)            # ('dados', 'relatorio_2024.txt') -- cada parte do caminho
```

## Verificando existência e tipo

```python
caminho = Path("dados/relatorio.txt")

print(caminho.exists())      # True/False
print(caminho.is_file())      # True se for um arquivo
print(caminho.is_dir())        # True se for uma pasta
```

## Criando diretórios

```python
pasta = Path("dados/relatorios/2024")
pasta.mkdir(parents=True, exist_ok=True)
```

- `parents=True`: cria também as pastas intermediárias que não existirem
  (`dados` e `dados/relatorios`, se ainda não existissem).
- `exist_ok=True`: não gera erro se a pasta já existir (sem isso,
  `mkdir()` levantaria `FileExistsError`).

## Lendo e escrevendo arquivos com `Path`

`Path` tem métodos convenientes que evitam abrir/fechar manualmente para
casos simples:

```python
caminho = Path("dados/nota.txt")
caminho.write_text("Reunião às 15h\n", encoding="utf-8")

conteudo = caminho.read_text(encoding="utf-8")
print(conteudo)
```

Para casos mais elaborados (leitura linha a linha, modos binários),
continue usando `with open(...)`, como no módulo 5 — `Path` também
funciona diretamente como argumento de `open()`:

```python
with open(caminho, "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
```

## Listando o conteúdo de uma pasta

```python
pasta = Path("dados")

for item in pasta.iterdir():
    print(item, "(pasta)" if item.is_dir() else "(arquivo)")
```

### Buscando arquivos por padrão com `glob`

```python
pasta = Path("dados")

for arquivo_txt in pasta.glob("*.txt"):        # todos os .txt diretamente em "dados"
    print(arquivo_txt)

for arquivo_txt in pasta.rglob("*.txt"):        # busca em todas as subpastas também
    print(arquivo_txt)
```

## `os` ainda é útil para algumas coisas

Embora `pathlib` seja preferido para manipulação de caminhos, o módulo
`os` continua relevante para outras tarefas do sistema:

```python
import os

print(os.getcwd())             # diretório de trabalho atual
print(os.environ.get("HOME"))   # variáveis de ambiente
os.rename("antigo.txt", "novo.txt")   # renomear (pathlib também tem Path.rename)
```

## Erros comuns

- Concatenar caminhos com `+` e `"/"` manualmente em vez de usar o
  operador `/` do `Path` — funciona "por acaso" em um sistema
  operacional e quebra em outro.
- Chamar `.mkdir()` sem `exist_ok=True` em um código que pode rodar mais
  de uma vez, e não tratar o `FileExistsError` resultante.
- Esquecer `parents=True` ao criar uma pasta cujos "pais" ainda não
  existem, causando `FileNotFoundError`.
- Usar `.read_text()`/`.write_text()` para arquivos muito grandes —
  esses métodos carregam o conteúdo inteiro na memória de uma vez; para
  arquivos grandes, prefira `open()` e ler por partes/linhas.

## Boas práticas

- Use `pathlib.Path` para qualquer manipulação de caminho em código
  novo — é mais legível e portátil entre sistemas operacionais que
  strings concatenadas.
- Use `mkdir(parents=True, exist_ok=True)` como padrão ao criar
  diretórios, a menos que você tenha um motivo específico para querer o
  erro em um desses casos.
- Combine `pathlib` para caminhos com `open()` tradicional (do módulo 5)
  quando precisar de controle fino sobre a leitura/escrita.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-07-biblioteca-padrao-util/aula-03-os-pathlib-e-sistema-de-arquivos/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: collections, itertools e functools](../aula-02-collections-itertools-e-functools/aula.md) · ➡️ [Próxima aula: logging e debugging](../aula-04-logging-e-debugging/aula.md)
