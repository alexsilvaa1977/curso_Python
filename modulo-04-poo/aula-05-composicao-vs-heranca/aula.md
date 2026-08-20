# Aula 5 — Composição vs. herança

**Objetivos desta aula:**
- Entender a diferença entre relação "é um" (herança) e "tem um"
  (composição).
- Reescrever um exemplo de herança mal aplicada usando composição.
- Saber decidir, na prática, quando usar cada abordagem.

## "É um" vs. "tem um"

- **Herança** modela uma relação "é um": `Cachorro` **é um** `Animal`,
  `Gerente` **é um** `Funcionario`. A subclasse deve ser genuinamente um
  caso especial da classe pai, podendo ser usada em qualquer lugar que
  espera a classe pai (o polimorfismo da aula 2).
- **Composição** modela uma relação "tem um": um `Carro` **tem um**
  `Motor`; um `Pedido` **tem uma** lista de `Item`. Em vez de herdar, o
  objeto guarda uma **instância de outra classe** como atributo.

```python
# Composição: Carro TEM UM Motor
class Motor:
    def __init__(self, potencia_cv):
        self.potencia_cv = potencia_cv

    def ligar(self):
        return "Motor ligado"

class Carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor          # Carro guarda um Motor como atributo

    def ligar(self):
        return f"{self.modelo}: {self.motor.ligar()}"

motor_v6 = Motor(300)
carro = Carro("Sedan X", motor_v6)
print(carro.ligar())    # 'Sedan X: Motor ligado'
```

## Um exemplo de herança mal aplicada

Um erro comum de quem está aprendendo POO é usar herança só porque
"parece" haver uma relação, sem checar se ela é genuína:

```python
# Problemático: um Passaro "tem" a capacidade de voar, mas nem todo
# passáro voa (pinguins, avestruzes) -- herdar de Voador força todo
# Passaro a "ser um" Voador, o que não é sempre verdade.
class Voador:
    def voar(self):
        return "voando..."

class Passaro(Voador):
    pass

class Pinguim(Passaro):
    def voar(self):
        raise NotImplementedError("Pinguins não voam!")   # sinal de que o design está errado
```

Se uma subclasse precisa **desabilitar** ou **contradizer** um
comportamento herdado, isso é um forte sinal de que a relação "é um" não
é verdadeira — e composição (ou uma hierarquia diferente) é mais
adequada.

## Reescrevendo com composição

```python
class CapacidadeVoo:
    def voar(self):
        return "voando..."

class Passaro:
    def __init__(self, nome, capacidade_voo=None):
        self.nome = nome
        self.capacidade_voo = capacidade_voo   # pode ser None

    def tentar_voar(self):
        if self.capacidade_voo is None:
            return f"{self.nome} não sabe voar."
        return f"{self.nome}: {self.capacidade_voo.voar()}"

aguia = Passaro("Águia", CapacidadeVoo())
pinguim = Passaro("Pinguim")    # sem capacidade de voo

print(aguia.tentar_voar())      # 'Águia: voando...'
print(pinguim.tentar_voar())     # 'Pinguim não sabe voar.'
```

Agora cada `Passaro` só "tem" a capacidade de voar se ela fizer sentido
para aquele pássaro específico — sem forçar uma hierarquia de classes
que não reflete a realidade.

## Um checklist rápido para decidir

Pergunte-se sobre a relação entre duas entidades:

1. "B é um tipo de A, sempre, sem exceções?" → tende a favorecer
   **herança** (`Gerente` é sempre um `Funcionario`).
2. "B usa/contém/depende de A, mas não é um tipo de A?" → favorece
   **composição** (`Carro` usa um `Motor`, mas um carro não é um motor).
3. "Preciso sobrescrever um método herdado para fazer o contrário do que
   ele faz, ou para lançar um erro dizendo 'isso não é suportado'?" →
   sinal de alerta: provavelmente a herança está sendo mal aplicada;
   considere composição.

Muitos desenvolvedores experientes seguem o princípio "prefira
composição a herança" como regra geral — não porque herança seja
"errada", mas porque composição costuma ser mais flexível e menos
propensa a hierarquias frágeis conforme o projeto cresce.

## Erros comuns

- Criar herança de 3+ níveis só para reaproveitar um método, quando
  composição resolveria de forma mais simples e flexível.
- Ignorar o sinal de alerta de uma subclasse que precisa "desligar" ou
  contradizer comportamento herdado.
- Achar que composição sempre substitui herança — em relações "é um"
  genuínas e estáveis (como `Gerente`/`Funcionario` no módulo desta
  aula), herança continua sendo a escolha mais direta e legível.

## Boas práticas

- Ao modelar uma nova classe, pergunte primeiro "isso é uma composição
  (tem um) ou uma especialização genuína (é um)?" antes de escolher.
- Prefira composição quando o comportamento pode variar de forma
  independente do "tipo" do objeto principal (como a capacidade de voo
  dos pássaros).
- Reserve herança para hierarquias estáveis e bem definidas, onde toda
  subclasse pode substituir a classe pai sem surpresas (o chamado
  "princípio de substituição").

---
➡️ [Exemplos práticos (notebook)](exemplos.ipynb) · [Exercícios](exercicios.md)
⬅️ [Aula anterior: Métodos especiais (dunder methods)](../aula-04-metodos-especiais-dunder/aula.md) · ➡️ [Próximo módulo: Tratamento de erros e arquivos](../../modulo-05-tratamento-de-erros-e-arquivos/README.md)
