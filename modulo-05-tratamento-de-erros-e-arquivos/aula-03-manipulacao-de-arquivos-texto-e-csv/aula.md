# Aula 3 — Manipulação de arquivos texto e CSV

**Objetivos desta aula:**
- Ler e escrever arquivos de texto com `open()` e `with`.
- Entender os modos de abertura (`r`, `w`, `a`).
- Ler e escrever arquivos CSV com o módulo `csv`.

## Abrindo arquivos com `open()`

```python
arquivo = open("notas.txt", "r")   # "r" = read (leitura)
conteudo = arquivo.read()
print(conteudo)
arquivo.close()                     # importante: sempre fechar o arquivo
```

Esquecer de fechar um arquivo pode causar problemas (dados não gravados
no disco, arquivo "travado" para outros programas). Por isso, a forma
recomendada é usar `with`:

```python
with open("notas.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# o arquivo é fechado automaticamente ao saír do bloco "with",
# mesmo que ocorra uma exceção dentro dele
```

## Modos de abertura

| Modo | Significado |
|---|---|
| `"r"` | leitura (erro se o arquivo não existir) |
| `"w"` | escrita — **sobrescreve** o arquivo todo, ou cria se não existir |
| `"a"` | *append* — adiciona ao final do arquivo, sem apagar o que já existe |
| `"r+"` | leitura e escrita |

```python
with open("log.txt", "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")

with open("log.txt", "a") as arquivo:
    arquivo.write("Linha adicionada depois, sem apagar as anteriores\n")
```

## Lendo arquivos linha por linha

```python
with open("notas.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())    # .strip() remove a quebra de linha "\n" do final
```

```python
with open("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()   # lista com todas as linhas
print(linhas)
```

## Tratando o arquivo que não existe

```python
try:
    with open("arquivo_que_nao_existe.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
```

## Trabalhando com CSV

CSV (*comma-separated values*) é um formato de texto simples para dados
tabulares (linhas e colunas), muito usado para exportar/importar
planilhas. O módulo `csv` da biblioteca padrão facilita ler e escrever
esse formato corretamente (lidando com vírgulas dentro de campos, etc.):

```python
import csv

with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["nome", "preco", "estoque"])       # cabeçalho
    escritor.writerow(["Teclado", 150.0, 20])
    escritor.writerow(["Mouse", 45.0, 50])
```

```python
import csv

with open("produtos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)     # cada linha é uma lista de strings
```

### `csv.DictReader` e `csv.DictWriter`

Mais conveniente quando você quer trabalhar com os dados como
dicionários (usando o cabeçalho como chaves):

```python
import csv

with open("produtos.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha["nome"], linha["preco"])   # acesso por nome de coluna
```

```python
import csv

with open("produtos.csv", "w", newline="", encoding="utf-8") as arquivo:
    campos = ["nome", "preco", "estoque"]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerow({"nome": "Teclado", "preco": 150.0, "estoque": 20})
```

## Erros comuns

- Esquecer de fechar o arquivo ao não usar `with` — sempre prefira
  `with open(...) as arquivo:`.
- Ler um arquivo CSV com `csv.reader` e tratar os valores como números
  diretamente — tudo que vem do CSV é **texto**; converta explicitamente
  (`float(linha["preco"])`) quando precisar calcular.
- Não usar `newline=""` ao escrever CSV no Windows — pode gerar linhas
  em branco extras (é uma particularidade do módulo `csv`; o parâmetro
  evita esse problema em qualquer sistema).
- Assumir que o arquivo sempre existe/tem o formato esperado — trate
  `FileNotFoundError` e valide os dados lidos.

## Boas práticas

- Sempre use `with` para abrir arquivos — garante o fechamento
  automático, mesmo com exceções.
- Para CSV, prefira `DictReader`/`DictWriter` quando os dados tiverem
  cabeçalho — o código fica mais legível (acesso por nome, não por
  posição).
- Especifique `encoding="utf-8"` explicitamente ao abrir arquivos de
  texto, para evitar problemas com acentuação em diferentes sistemas.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Exceções customizadas](../aula-02-excecoes-customizadas/aula.md) · ➡️ [Próxima aula: Serialização: JSON e pickle](../aula-04-serializacao-json-e-pickle/aula.md)
