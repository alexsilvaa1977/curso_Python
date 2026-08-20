# Aula 4 — logging e debugging

**Objetivos desta aula:**
- Entender por que `logging` é preferível a `print` para diagnóstico.
- Configurar níveis de log e usar `getLogger`.
- Ter uma introdução prática ao depurador (`breakpoint()`/`pdb`).

## O problema de depurar só com `print`

Até agora, você provavelmente usou `print()` para entender o que está
acontecendo dentro do código (`print("chegou aqui")`,
`print(variavel)`). Funciona para scripts pequenos, mas tem limitações:

- Não tem "níveis" — não dá para distinguir uma mensagem informativa de
  um erro grave sem convenção manual.
- É difícil desligar todos os `print` de depuração de uma vez sem
  apagá-los um por um.
- Não registra automaticamente data/hora, nem de onde a mensagem veio.

## `logging`: a ferramenta certa para isso

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Programa iniciado")
logging.warning("Configuração não encontrada, usando padrão")
logging.error("Falha ao conectar ao banco de dados")
```

Saída (formato padrão):
```
INFO:root:Programa iniciado
WARNING:root:Configuração não encontrada, usando padrão
ERROR:root:Falha ao conectar ao banco de dados
```

## Níveis de log

Do menos ao mais grave:

| Nível | Quando usar |
|---|---|
| `DEBUG` | detalhes técnicos, úteis só durante desenvolvimento |
| `INFO` | eventos normais do fluxo do programa |
| `WARNING` | algo inesperado, mas o programa continua funcionando |
| `ERROR` | uma operação falhou |
| `CRITICAL` | erro grave, o programa pode não conseguir continuar |

```python
logging.basicConfig(level=logging.WARNING)   # só mostra WARNING e acima

logging.info("Isso NÃO vai aparecer, nível abaixo do configurado")
logging.warning("Isso VAI aparecer")
```

Configurar o nível permite "silenciar" mensagens menos importantes em
produção, sem apagar o código de logging — muito mais flexível que
comentar/descomentar `print`.

## `getLogger`: um logger por módulo

Em projetos maiores, cada módulo cria seu próprio logger, nomeado com
`__name__` — isso permite saber exatamente de onde cada mensagem veio:

```python
# arquivo: pagamentos.py
import logging

logger = logging.getLogger(__name__)

def processar_pagamento(valor):
    logger.info(f"Processando pagamento de {valor}")
    if valor <= 0:
        logger.error(f"Valor inválido: {valor}")
        raise ValueError("Valor de pagamento deve ser positivo")
    logger.info("Pagamento processado com sucesso")
```

```python
# arquivo: main.py
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s: %(message)s")

from pagamentos import processar_pagamento
processar_pagamento(100)
```

Saída:
```
2026-08-20 14:35:02 pagamentos INFO: Processando pagamento de 100
2026-08-20 14:35:02 pagamentos INFO: Pagamento processado com sucesso
```

O formato `%(asctime)s %(name)s %(levelname)s: %(message)s` mostra
data/hora, o nome do módulo (`pagamentos`, vindo de `__name__`), o nível
e a mensagem — informação que `print()` não te dá de graça.

## `logging.exception`: registrando erros com o traceback completo

Dentro de um `except`, `logging.exception` registra a mensagem **e** o
traceback completo do erro, o que é extremamente útil para depurar
problemas em produção depois que já aconteceram:

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    logging.exception("Erro ao calcular resultado")
    # registra a mensagem + o traceback completo, sem precisar de mais código
```

## `print` de depuração vs. depurador de verdade

Para investigar um bug complexo, alternar `print()` em vários pontos e
rodar de novo repetidamente é lento. O depurador (*debugger*) permite
**pausar** a execução em um ponto específico e inspecionar variáveis
interativamente:

```python
def calcular_desconto(preco, percentual):
    breakpoint()          # a execução pausa aqui
    desconto = preco * percentual / 100
    return preco - desconto
```

Ao rodar o script no terminal, a execução para na linha do
`breakpoint()` e abre um prompt interativo (`(Pdb)`) onde você pode:

```
(Pdb) preco
100
(Pdb) percentual
10
(Pdb) n        # "next" -- executa a próxima linha
(Pdb) desconto
10.0
(Pdb) c        # "continue" -- continua a execução normalmente
```

Comandos úteis do `pdb`: `n` (próxima linha), `s` (entrar dentro de uma
chamada de função), `c` (continuar até o próximo `breakpoint()` ou o
fim), `p variavel` (imprimir uma variável), `q` (sair).

Em notebooks Jupyter e em editores modernos (VS Code, PyCharm), você
normalmente usa o depurador visual do próprio editor em vez do `pdb` no
terminal — mas o conceito (pausar e inspecionar) é o mesmo.

## Erros comuns

- Deixar `print()` de depuração espalhados pelo código em produção —
  além de poluir a saída, não há como desligá-los seletivamente.
- Configurar `logging.basicConfig` mais de uma vez em módulos diferentes
  — geralmente só a primeira chamada tem efeito; configure uma vez, no
  ponto de entrada do programa (`main.py`).
- Usar `print` para registrar erros importantes que você vai precisar
  investigar depois — sem timestamp, sem nível, sem traceback
  automático.

## Boas práticas

- Prefira `logging` a `print` para qualquer mensagem que não seja uma
  saída **intencional** do programa para o usuário final.
- Use `logger = logging.getLogger(__name__)` em cada módulo, em vez de
  chamar `logging.info(...)` diretamente em projetos maiores.
- Use `logging.exception()` dentro de blocos `except` quando quiser
  registrar o erro para investigação posterior.
- Aprenda o básico de `breakpoint()`/`pdb` (ou o debugger do seu editor)
  — é mais eficiente que `print` para bugs difíceis de reproduzir.

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: os, pathlib e sistema de arquivos](../aula-03-os-pathlib-e-sistema-de-arquivos/aula.md) · ➡️ [Próximo módulo: Web e APIs](../../modulo-08-web-e-apis/README.md)
