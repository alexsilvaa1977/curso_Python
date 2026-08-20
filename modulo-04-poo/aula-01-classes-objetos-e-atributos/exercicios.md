# Exercícios — Aula 1: Classes, objetos e atributos

1. Crie uma classe `Produto` com atributos `nome` e `preco`, e um método
   `exibir()` que imprime `"nome - R$ preco"`.

2. Crie uma classe `Carro` com atributos `marca`, `modelo` e
   `quilometragem` (iniciando em 0), e um método `rodar(km)` que aumenta
   a quilometragem.

3. Adicione à classe `Pessoa` da aula um método `eh_maior_de_idade()` que
   retorna `True`/`False` com base em `self.idade`.

4. Crie uma classe `Retangulo` com `largura` e `altura`, e métodos
   `calcular_area()` e `calcular_perimetro()`.

5. Adicione um atributo de classe `MOEDA = "R$"` à classe `Produto` do
   exercício 1, e use-o no método `exibir()` em vez de escrever `"R$"`
   fixo no texto.

6. **Desafio:** crie uma classe `Fila` que representa uma fila de
   atendimento, com uma lista interna de nomes. Métodos:
   `entrar_na_fila(nome)` (adiciona ao fim), `chamar_proximo()` (remove e
   retorna o primeiro da fila, ou `None` se estiver vazia), e
   `total_na_fila()` (retorna quantas pessoas estão esperando).

---
⬅️ [Voltar para a aula](aula.md)
