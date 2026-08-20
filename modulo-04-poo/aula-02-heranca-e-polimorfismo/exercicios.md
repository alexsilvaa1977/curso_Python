# Exercícios — Aula 2: Herança e polimorfismo

1. Crie uma classe `FormaGeometrica` com um método `calcular_area()` que
   retorna `0` (comportamento padrão). Crie duas subclasses,
   `Quadrado` e `Circulo`, cada uma sobrescrevendo `calcular_area()` com
   a fórmula correta.

2. Crie uma classe `Veiculo` com `__init__(self, marca, modelo)` e um
   método `descricao()`. Crie uma subclasse `Moto` que adiciona um
   atributo `cilindradas`, usando `super().__init__(...)`.

3. Dada uma lista com objetos de classes diferentes que todas têm um
   método `emitir_som()` (como na aula), escreva um `for` que chama
   `emitir_som()` de cada um sem usar `isinstance` ou `if`.

4. Verifique, com `isinstance()`, se um objeto `Quadrado` do exercício 1
   também é considerado uma instância de `FormaGeometrica`.

5. Crie uma classe `Funcionario` e uma subclasse `FuncionarioComissionado`
   que sobrescreve `calcular_salario()` para somar uma comissão sobre
   vendas ao salário base (reaproveitando `super().calcular_salario()`).

6. **Desafio:** crie uma hierarquia `ContaBancaria` -> `ContaPoupanca` e
   `ContaCorrente`. `ContaPoupanca` tem um método `aplicar_rendimento(taxa)`
   que aumenta o saldo por um percentual. `ContaCorrente` tem um
   `limite_cheque_especial` e permite saldo negativo até esse limite no
   método `sacar(valor)` (sobrescrito).

---
⬅️ [Voltar para a aula](aula.md)
