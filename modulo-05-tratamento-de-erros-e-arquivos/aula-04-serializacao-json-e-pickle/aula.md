# Aula 4 — Serialização: JSON e pickle

**Objetivos desta aula:**
- Converter dados Python para JSON e vice-versa.
- Salvar e carregar JSON em arquivo.
- Entender o que é `pickle` e por que usá-lo com cuidado.

## O que é serialização

Serializar é converter uma estrutura de dados (dicionário, lista, objeto)
em um formato que pode ser salvo em arquivo ou enviado pela rede — e
depois reconstruído (desserializado). É essencial para persistir dados
entre execuções do programa, ou para uma API se comunicar com outro
sistema (assunto do módulo 8).

## JSON: o formato mais comum

JSON (*JavaScript Object Notation*) é um formato de texto legível por
humanos, amplamente usado em APIs web e arquivos de configuração. Mapeia
quase diretamente para dicionários e listas do Python:

```python
import json

dados = {
    "nome": "Ana",
    "idade": 28,
    "linguagens": ["Python", "SQL"],
    "ativo": True,
}

texto_json = json.dumps(dados)     # converte dict Python -> string JSON
print(texto_json)
# '{"nome": "Ana", "idade": 28, "linguagens": ["Python", "SQL"], "ativo": true}'
```

```python
texto_json = '{"nome": "Bruno", "idade": 34}'
dados = json.loads(texto_json)      # converte string JSON -> dict Python
print(dados["nome"], dados["idade"])
```

Note as diferenças de sintaxe entre JSON e Python: JSON usa `true`/
`false`/`null` (minúsculo), Python usa `True`/`False`/`None`. A
conversão entre esses formatos é feita automaticamente por `json.dumps`/
`json.loads`.

### `json.dumps` com formatação legível

```python
texto_formatado = json.dumps(dados, indent=2, ensure_ascii=False)
print(texto_formatado)
```

`indent=2` deixa o JSON legível (com quebras de linha e indentação);
`ensure_ascii=False` permite que acentos apareçam como caracteres
normais, em vez de códigos de escape (`á` para "á").

## Salvando e carregando JSON em arquivo

```python
import json

dados = {"nome": "Ana", "idade": 28}

with open("pessoa.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)   # note: dump (sem "s"), escreve direto no arquivo
```

```python
with open("pessoa.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)     # note: load (sem "s"), lê direto do arquivo
print(dados)
```

Resumindo a nomenclatura do módulo `json`: os que terminam em `s`
(`dumps`/`loads`) trabalham com **strings** em memória; os sem `s`
(`dump`/`load`) trabalham direto com um **arquivo aberto**.

## Limitações do JSON

JSON só representa tipos básicos: números, strings, booleanos, `null`,
listas e objetos (dicionários com chaves string). Não é possível
serializar diretamente, por exemplo, um objeto de uma classe customizada
sem primeiro convertê-lo para um dicionário:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

ana = Pessoa("Ana", 28)

# json.dumps(ana)   # ERRO: TypeError, objeto Pessoa não é serializável

dados = {"nome": ana.nome, "idade": ana.idade}
print(json.dumps(dados))   # funciona, porque agora é um dict simples
```

## `pickle`: serializando objetos Python arbitrários

`pickle` é um módulo da biblioteca padrão que consegue serializar quase
qualquer objeto Python (incluindo instâncias de classes customizadas),
mas em um formato **binário**, específico do Python — não legível por
humanos e não compatível com outras linguagens:

```python
import pickle

ana = Pessoa("Ana", 28)

with open("pessoa.pkl", "wb") as arquivo:    # "wb" = write binary
    pickle.dump(ana, arquivo)

with open("pessoa.pkl", "rb") as arquivo:     # "rb" = read binary
    ana_recuperada = pickle.load(arquivo)

print(ana_recuperada.nome, ana_recuperada.idade)
```

### O aviso de segurança do `pickle`

**Nunca use `pickle.load()` em dados que vieram de uma fonte não
confiável** (um arquivo baixado da internet, um dado recebido de um
usuário externo). Carregar um pickle malicioso pode executar código
arbitrário na sua máquina — é um risco de segurança real, não teórico.
Use `pickle` apenas para dados que você mesmo gerou e controla (ex.:
cache interno do seu próprio programa).

## Quando usar JSON vs. pickle

| Situação | Prefira |
|---|---|
| Comunicação com API web, arquivo de configuração | **JSON** |
| Dado precisa ser lido por outra linguagem/sistema | **JSON** |
| Serializar objetos Python complexos (só para uso interno) | `pickle` (com cautela) |
| Dado vem de fonte não confiável | **Nunca `pickle`** — use JSON e valide |

## Erros comuns

- Tentar serializar um objeto de classe customizada direto com
  `json.dumps` sem convertê-lo para dicionário primeiro.
- Usar `pickle.load()` em arquivos de origem desconhecida — risco de
  segurança.
- Esquecer o modo binário (`"wb"`/`"rb"`) ao usar `pickle` — usar `"w"`/
  `"r"` (texto) com pickle gera erro, porque o conteúdo é binário.
- Confundir `dump`/`dumps` e `load`/`loads` — lembre-se: com `s` = string
  em memória, sem `s` = arquivo.

## Boas práticas

- Prefira JSON sempre que possível — é legível, seguro e interoperável.
- Reserve `pickle` para dados internos do seu próprio programa, nunca
  para dados externos/não confiáveis.
- Ao salvar JSON legível para humanos (arquivos de configuração, por
  exemplo), use `indent=2` e `ensure_ascii=False`.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) ([abrir no Colab](https://colab.research.google.com/github/alexsilvaa1977/curso_Python/blob/main/modulo-05-tratamento-de-erros-e-arquivos/aula-04-serializacao-json-e-pickle/exemplos.ipynb)) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Manipulação de arquivos texto e CSV](../aula-03-manipulacao-de-arquivos-texto-e-csv/aula.md) · ➡️ [Próximo módulo: Testes e qualidade](../../modulo-06-testes-e-qualidade/README.md)
